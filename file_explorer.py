import os
import msvcrt
import shutil
import subprocess
from datetime import datetime
import curses
import textwrap
import platform
from PIL import Image
import io

def safe_addstr(stdscr, y, x, string):
    """Safely add string to window, handling boundary errors"""
    height, width = stdscr.getmaxyx()
    try:
        if y < height and x < width:
            maxlen = width - x - 1
            if maxlen > 0:
                stdscr.addstr(y, x, string[:maxlen])
    except:
        pass

def init_colors():
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)    # Selected item
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Directories
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)   # Default files
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)     # PDFs
    curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_BLACK)    # Images
    curses.init_pair(6, curses.COLOR_GREEN, curses.COLOR_BLACK)   # Text files
    curses.init_pair(7, curses.COLOR_MAGENTA, curses.COLOR_BLACK) # Office documents

def get_file_color(filename):
    ext = os.path.splitext(filename)[1].lower()
    if ext in ['.pdf']:
        return curses.color_pair(4)
    elif ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
        return curses.color_pair(5)
    elif ext in ['.txt', '.log', '.md']:
        return curses.color_pair(6)
    elif ext in ['.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx']:
        return curses.color_pair(7)
    else:
        return curses.color_pair(3)

def get_file_preview(file_path, max_width, max_height):
    if not os.path.exists(file_path):
        return ["File not found"]
    
    file_ext = os.path.splitext(file_path)[1].lower()
    
    try:
        if file_ext == '.txt':
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                wrapped_lines = []
                for line in content.split('\n'):
                    wrapped_lines.extend(textwrap.wrap(line, max_width-2) or [''])
                return wrapped_lines[:max_height]
        
        elif file_ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
            return ["Image file:", file_path, "", "Size: " + str(os.path.getsize(file_path) / 1024) + " KB"]
        
        elif file_ext == '.pdf':
            return ["PDF file:", file_path, "", "Size: " + str(os.path.getsize(file_path) / 1024) + " KB"]
        
        elif file_ext in ['.doc', '.docx']:
            return ["Word document:", file_path, "", "Size: " + str(os.path.getsize(file_path) / 1024) + " KB"]
        
        else:
            return ["Binary file:", file_path, "", "Size: " + str(os.path.getsize(file_path) / 1024) + " KB"]
            
    except Exception as e:
        return [f"Error previewing file: {str(e)}"]

def open_file(file_path):
    try:
        if platform.system() == 'Windows':
            os.startfile(file_path)
        else:
            subprocess.call(('xdg-open', file_path))
        return "Opening file..."
    except Exception as e:
        return f"Error opening file: {str(e)}"

def main(stdscr):
    try:
        curses.curs_set(0)  # Hide cursor
        init_colors()
        
        current_path = os.getcwd()
        selected_index = 0
        preview_offset = 0
        list_offset = 0
        status_message = ""
        split_ratio = 0.33
        
        while True:
            try:
                height, width = stdscr.getmaxyx()
                list_width = int(width * split_ratio)
                preview_width = width - list_width - 1
                max_display_items = height - 4
                
                try:
                    items = sorted(os.listdir(current_path))
                except:
                    items = ['.']
                
                if selected_index - list_offset >= max_display_items:
                    list_offset = selected_index - max_display_items + 1
                elif selected_index < list_offset:
                    list_offset = selected_index
                
                stdscr.clear()
                
                # Draw vertical separator
                for i in range(height-1):
                    safe_addstr(stdscr, i, list_width, "│")
                
                # Display current path
                path_display = f" {current_path}"
                if len(path_display) > list_width:
                    path_display = "..." + path_display[-(list_width-5):]
                safe_addstr(stdscr, 0, 0, path_display[:list_width])
                safe_addstr(stdscr, 1, 0, "─" * list_width)
                
                # Display items with scrolling
                visible_items = items[list_offset:list_offset + max_display_items]
                for i, item in enumerate(visible_items):
                    if i + 3 >= height:
                        break
                    
                    real_index = i + list_offset
                    full_path = os.path.join(current_path, item)
                    is_dir = os.path.isdir(full_path)
                    
                    if real_index == selected_index:
                        stdscr.attron(curses.color_pair(1))
                    elif is_dir:
                        stdscr.attron(curses.color_pair(2))
                    else:
                        stdscr.attron(get_file_color(item))
                    
                    item_display = f" {'[DIR] ' if is_dir else ''}{item}"
                    if len(item_display) > list_width - 2:
                        item_display = item_display[:list_width-5] + "..."
                    
                    safe_addstr(stdscr, i + 2, 0, item_display)
                    
                    if real_index == selected_index:
                        stdscr.attroff(curses.color_pair(1))
                    elif is_dir:
                        stdscr.attroff(curses.color_pair(2))
                    else:
                        stdscr.attroff(get_file_color(item))
                
                # Show scroll indicators
                if list_offset > 0:
                    safe_addstr(stdscr, 2, list_width - 2, "↑")
                if list_offset + max_display_items < len(items):
                    safe_addstr(stdscr, min(height-2, max_display_items+1), list_width - 2, "↓")
                
                # Display preview
                if items:
                    selected_item = items[selected_index]
                    full_path = os.path.join(current_path, selected_item)
                    
                    if os.path.isfile(full_path):
                        preview_lines = get_file_preview(full_path, preview_width, height-3)
                        for i, line in enumerate(preview_lines[preview_offset:]):
                            if i + 2 >= height:
                                break
                            safe_addstr(stdscr, i + 2, list_width + 2, line[:preview_width-2])
                
                # Display status and controls
                if status_message:
                    safe_addstr(stdscr, height-1, 0, status_message[:width-1])
                
                controls = " ↑↓:Nav | Enter:Open | Back:Up | [:Shrink ]:Expand | Q:Quit "
                safe_addstr(stdscr, height-1, max(0, width-len(controls)-1), controls)
                
                try:
                    stdscr.refresh()
                except:
                    pass
                
                # Input handling
                key = stdscr.getch()
                
                if key == curses.KEY_UP:
                    if selected_index > 0:
                        selected_index -= 1
                        preview_offset = 0
                elif key == curses.KEY_DOWN:
                    if selected_index < len(items) - 1:
                        selected_index += 1
                        preview_offset = 0
                elif key == ord('\n'):
                    selected_item = items[selected_index]
                    full_path = os.path.join(current_path, selected_item)
                    
                    if os.path.isdir(full_path):
                        try:
                            current_path = full_path
                            selected_index = 0
                            list_offset = 0
                            preview_offset = 0
                        except:
                            status_message = "Cannot access directory"
                    else:
                        status_message = open_file(full_path)
                elif key == ord('\b') or key == 127 or key == curses.KEY_BACKSPACE:
                    current_path = os.path.dirname(current_path)
                    selected_index = 0
                    list_offset = 0
                    preview_offset = 0
                elif key == ord('['):
                    split_ratio = max(0.1, split_ratio - 0.05)
                elif key == ord(']'):
                    split_ratio = min(0.9, split_ratio + 0.05)
                elif key == curses.KEY_PPAGE:
                    preview_offset = max(0, preview_offset - (height-3))
                elif key == curses.KEY_NPAGE:
                    preview_offset += height-3
                elif key == ord('q') or key == ord('Q'):
                    break
            
            except curses.error:
                stdscr.clear()
                continue
    
    except Exception as e:
        curses.endwin()
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    curses.wrapper(main)