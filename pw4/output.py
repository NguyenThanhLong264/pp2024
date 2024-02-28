import curses

def initialize_curses():
    stdscr = curses.initscr()
    curses.cbreak()
    curses.noecho()
    stdscr.keypad(True)
    return stdscr

def close_curses(stdscr):
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

def display_menu(stdscr):
    stdscr.addstr("\n===== MENU =====\n")
    stdscr.addstr("1. Input data for students\n")
    stdscr.addstr("2. Input courses\n")
    stdscr.addstr("3. List students\n")
    stdscr.addstr("4. List courses\n")
    stdscr.addstr("5. Choose course for students\n")
    stdscr.addstr("6. Show students mark\n")
    stdscr.addstr("0. Exit\n")
    stdscr.refresh()

def display_message(stdscr, message):
    stdscr.addstr(message)
    stdscr.refresh()