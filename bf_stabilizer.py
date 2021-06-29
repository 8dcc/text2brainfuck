import re, sys

#######  EDIT ME  #######
debug = False           # Boolean. Print the process on the screen.
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
    regular_expression = re.compile("([>.<,+-\[\]]{60})")
    with open(str(check_file_argv()), "r") as reader:
        while True:
            line = reader.readline()
            if not line:
                break
            if (" " not in line) or (line is not "\n"):
                results = regular_expression.findall(line)
                remaining_characters_count = len(line.strip()) - (len(results) * 60)
                remaining_characters = line
                for n in results:
                    if debug:
                        print(n)
                    with open("stabilized.bf", "a") as append:
                        append.write(n + "\n")
                    if remaining_characters_count is not 0:
                        remaining_characters = remaining_characters.replace(n, "")
                if remaining_characters_count is not 0:
                    with open("stabilized.bf", "a") as append:
                        append.write(remaining_characters + "\n")
                if debug:
                    print(remaining_characters)
            else:
                with open("stabilized.bf", "a") as append:
                    append.write(line)

main()
