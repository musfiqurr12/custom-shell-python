import sys


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

        print(f"{command}: command not found")

if __name__ == "__main__":
    main()
