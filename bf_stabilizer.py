import re, sys

#######  EDIT ME  #######
enable_debug = True    # Boolean. Print the process on the screen.
#########################

def check_file_argv():
    if len(sys.argv) == 2:
        try:
            with open(sys.argv[1], "r") as check:
                check.readline()
        except Exception:
            print("\n [!] There was an error while reading the file.")
            exit(1)
        with open("stabilized.bf", "w") as writer:
            writer.write("[ Stabilized using https://github.com/r4v0l1/text2brainfuck ]\n\n")
        return sys.argv[1]
    else:
        print("\n [!] You need to input the file name as an argument. Nothing else!")
        exit(1)

def main():
    global enable_debug
    regular_expression = re.compile("([>.<,+-\[\]]{60})")
    with open(str(check_file_argv()), "r") as reader:
        while True:
            remaining_characters_count = 0
            line = reader.readline()
            if not line:
                break
            elif (" " not in line) or (line is not "\n"):
                results = regular_expression.findall(line.strip())
                results_mult = len(results) * 60
                remaining_characters_count = len(line.strip()) - results_mult
                for n in results:
                    if enable_debug:
                        print(n)
                    with open("stabilized.bf", "a") as append:
                        append.write(n + "\n")
                if remaining_characters_count is not 0:
                    remaining_characters = line[-remaining_characters_count:]
                    with open("stabilized.bf", "a") as append:
                        append.write(remaining_characters + "\n")
                if enable_debug:
                    print(remaining_characters)
                    print()
                    print("^" + " " * (remaining_characters_count - 2) + "^")
                    print(" REMAINING CHARACTERS: " + str(remaining_characters_count))
            else:
                with open("stabilized.bf", "a") as append:
                    append.write(line)

main()
