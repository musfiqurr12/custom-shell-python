import sys

builtins = ["exit", "echo", "type"]

def main():

    while True:
        sys.stdout.write("$ ")

        args = input().split()
        command = args[0]

        if command == "exit":
            break
        
        if command == "echo":
            print(" ".join(args[1:]))
            continue

        if command == "type":
            command_type = args[1]

            if command_type in builtins:
                print(f"{command_type} is a shell builtin")
            else:
                print(f"{command_type}: not found")

            continue

        print(f"{command}: command not found")
        
if __name__ == "__main__":
    main()
