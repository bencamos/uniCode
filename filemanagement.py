#File management
#
#ICTPRG407 | Learning Activity 3
import os
import sys
import StringIO
import time
import readline
import keyboard


def menu():
    print("Commands:\n     create file: touch {file name}\n     remove file: rm {file name}\n     move file: {old file} {new file}\n     edit file: edit {file name}")

def rlinput(text):
   prefill = text;
   readline.set_startup_hook(lambda: readline.insert_text(prefill))
   try:
      return raw_input("")
   finally:
      readline.set_startup_hook()

print("File management | ICTPRG407\nDesigned for linux")

menu();


while 1:
    x = raw_input(">> ")
    arr = x.split(" ")
    cmd = arr[0];
    name = arr[1];
    done = 0;

    # Python needs proper switches.
    if cmd == "touch":
        os.system("touch " + name)
    if cmd == "rm":
        os.system("rm -rf " + name)
    if cmd == "mv":
        os.system("mv " + name + " " + arr[2])
    if cmd == "edit":
        file = open(name, "r")
        text = file.read();
        file.close()
        while True:
            try:
                os.system("clear");
                print("Use control + c to save and exit\n================================");
                text = rlinput(text)
                text += "\n"
            except KeyboardInterrupt:
                file = open(name, "w")
                file.write(text);
                file.close()
                print()
                break