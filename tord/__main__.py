import sys
import os
# from .classm
# odule import MyClass
# from .funcmodule import my_function
def main():
    try:
        cmd = sys.argv[1]
        message = sys.argv[2:]
        if len(message) < 1:
            print('YEEEEEEEEEEEEEEEt')
        if cmd == 'push':
            try:
                commit_m = "'"
                for word in message:
                    commit_m += word + "_"
                commit_m = commit_m[:-1]
                commit_m += "'"
                query = "git status && git add . && git commit -m " + commit_m + " && git push"
                os.system(query)
            except:
                print('Failed to push to git')
        else:
            print('Invalid push command')
    except:
        print("vaild commands: 'push'")
if __name__ == '__main__':
    main()