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
            raw = args.message
            message = "'" + raw[0] +  "'"
            message = " -m ngfngf -m kmfkdmfm"
            query = "git status && git add . && git commit -m $" + message + " && git push"
            print(query)
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