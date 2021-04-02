from pynput.keyboard import Key, Listener, KeyCode, Controller
import time



run = 'q'
timeout = 0.1
thingSwitch = '2'
editKey = 'k'
resetEditKey ='j'



reset_key = KeyCode(char=run)
keyboard = Controller()

def on_press(key):
    if key == reset_key:
        keyboard.press(thingSwitch)
        keyboard.release(thingSwitch)

        time.sleep(timeout) 
        
        keyboard.press(editKey)
        keyboard.release(editKey)
        
        time.sleep(timeout)

        keyboard.press(resetEditKey)
        keyboard.release(resetEditKey)

        time.sleep(timeout)

        keyboard.press(editKey)
        keyboard.release(editKey)

with Listener(on_press=on_press) as listener:
    listener.join()
