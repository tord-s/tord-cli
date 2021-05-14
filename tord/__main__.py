import sys
import os
# from .classm
# odule import MyClass
# from .funcmodule import my_function
def main():
    cmd = sys.argv[1]
    message = sys.argv[2:]
    if cmd == 'push':
        try:
            commit_m = "'"
            for word in message:
                commit_m += word + "_"
            commit_m = commit_m.strip()
            commit_m += "'"
            query = "git status && git add . && git commit -m " + commit_m + " && git push"
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