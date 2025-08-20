import curses

def main(stdscr):
    # Setup
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)   # Non-blocking input
    stdscr.timeout(100) # Timeout for getch()
    
    height, width = stdscr.getmaxyx()
    player_x = width // 2
    player_y = height // 2
    
    while True:
        # Clear screen
        stdscr.clear()
        
        # Draw game area
        for y in range(height - 1):
            for x in range(width - 1):
                if x == player_x and y == player_y:
                    stdscr.addch(y, x, '^')
                else:
                    stdscr.addch(y, x, '.')
        
        # Instructions
        stdscr.addstr(height-1, 0, "Arrow keys to move, 'q' to quit")
        
        # Get input
        key = stdscr.getch()
        
        # Handle movement
        if key == curses.KEY_UP and player_y > 0:
            player_y -= 1
        elif key == curses.KEY_DOWN and player_y < height - 2:
            player_y += 1
        elif key == curses.KEY_LEFT and player_x > 0:
            player_x -= 1
        elif key == curses.KEY_RIGHT and player_x < width - 2:
            player_x += 1
        elif key == ord('q'):
            break
        
        stdscr.refresh()

# Run the game
curses.wrapper(main)