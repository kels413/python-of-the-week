import os

print("press ctr/command D to exit prompt")
try:
    while True:
        path = input("Please enter directory Path (absolute or relative) to view the output: ")
        if path == "~":
            print("this is it")
        if os.path.exists(path):
            expand_path = os.path.expanduser(path)
            content = os.listdir(expand_path)
            for cnt in content:
                if not cnt.startswith("."):
                    print(cnt)
except (EOFError, KeyboardInterrupt):
    print("\nGood bye!")
