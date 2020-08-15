#! python3
# mouseNow.py - Displays the mouse cursor's current position.

import pyautogui
print('Press Ctrl-C to quit.')

try:
    while True:
        # Get and print mouse coordinates
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr)
        
       # What to print when you leave the loop 
except KeyboardInterrupt:
    print('\nDone.')
    print('\b' * len(positionStr), end='', flush=True)
