import sys
import os
import argparse
# from .classm
# odule import MyClass
# from .funcmodule import my_function
def main():
    parser = argparse.ArgumentParser(description='Command to do')
    parser.add_argument('command', type=str,
                    help='available commands')
    parser.add_argument('param1', type=str,
                    help='first param')
    args = parser.parse_args()
    cmd = args.command
    if cmd == 'push':
        param1 = args.param1
        query = "git add . && git commit -m " + param1
        os.system(query)
    else:
        print('failure')
    # my_function('hello world')
    # my_object = MyClass('Thomas')
    # my_object.say_name()
    # os.system("git add . && git commit -m")
if __name__ == '__main__':
    main()