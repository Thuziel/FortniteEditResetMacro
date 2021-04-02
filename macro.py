from pynput.keyboard import Key, Listener, KeyCode, Controller
import time

run = 'q'
close = '0'
inventorySlot = '2'
editKey = 'k'
resetEditKey ='j'

timeout = 0.1

quit_key = KeyCode(char=close)
reset_key = KeyCode(char=run)
keyboard = Controller()

print("Marco successfully setup.\n")
print("Controls:\n    "+run+" to run\n    "+close+" to close\n")
print("Current Fortnite keybinds:\n    "+inventorySlot+" what inventory slot it switches to\n    "+editKey+" to edit\n    "+resetEditKey+" to reset edits\n")
print("If you would like to change any of these you can do so on lines 4-8.")

def on_press(key):
    if key == reset_key:
        keyboard.press(inventorySlot)
        keyboard.release(inventorySlot)

        time.sleep(timeout) 
        
        keyboard.press(editKey)
        keyboard.release(editKey)
        
        time.sleep(timeout)

        keyboard.press(resetEditKey)
        keyboard.release(resetEditKey)

        time.sleep(timeout)

        keyboard.press(editKey)
        keyboard.release(editKey)
    if key == quit_key:
        quit()

with Listener(on_press=on_press) as listener:
    listener.join()
