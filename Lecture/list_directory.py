import os

print("press ctr/command D to exit prompt")
try:
    while True:
        path = input("Please enter directory Path (absolute or relative) to view the output: ")
        # check if the path exists and also a tilde so we expand
        if os.path.exists(path) or path == "~":
            expand_path = os.path.expanduser(path)
            content = os.listdir(expand_path)
            # Display Non-hidden file
            for cnt in content:
                if not cnt.startswith("."):
                    print(cnt)
except (EOFError, KeyboardInterrupt):
    print("\nGood bye!")
