import sys
import os
import argparse
# from .classm
# odule import MyClass
# from .funcmodule import my_function
def main():
    parser = argparse.ArgumentParser(description='Command to do')
    parser.add_argument('command', type=str, help='available commands')
    parser.add_argument("-m", "--message", required=False,
	help="name of the user", nargs='+')
    args = parser.parse_args()
    cmd = args.command
    if cmd == 'push':
        try:
            raw = args.message[0].split(' ')
            message = ""
            for i in raw:
                message += '_' + i.strip()
            print(message)
            query = "git status && git add . && git commit -m " + message + " && git push"
            os.system(query)
        except:
            print('something else')
        


    else:
        print('failure')
    # my_function('hello world')
    # my_object = MyClass('Thomas')
    # my_object.say_name()
    # os.system("git add . && git commit -m")
if __name__ == '__main__':
    main()