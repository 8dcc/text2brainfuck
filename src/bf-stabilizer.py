# https://github.com/r4v10l1/text2brainfuck
# https://gist.github.com/r4v10l1/34a13e265b528c4975a719abed3d45a0
import re, sys, string

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
            # Edgy watermark
            writer.write("[ Stabilized using https://github.com/r4v0l1/text2brainfuck ]\n\n")
        return sys.argv[1]
    else:
        print("\n [!] You need to input the file name as an argument. Nothing else!")
        exit(1)

def main():
    global enable_debug
    remaining_characters_count = 0  # Define the value before using it
    # The regex value for the 60 characters we will use in each line
    regular_expression = re.compile("([>.<,+-\[\]]{60})")
    with open(str(check_file_argv()), "r") as reader:
        while True:
            line = reader.readline()
            if not line:
                break
            # Check if there is an invalid character in the line (leters or an empty line)
            if (any(char in line for char in string.ascii_letters)) or (line == "\n"):
                with open("stabilized.bf", "a") as append:
                    # Don't change that line
                    append.write(line)
            # If the line is valid
            else:
                # Search every 60 characters
                results = regular_expression.findall(line.strip())
                # Check the total characters, then check if there are any characters left
                results_mult = len(results) * 60
                remaining_characters_count = len(line.strip()) - results_mult
                # Write every result (set of 60 characters) in a line until there are no left
                for n in results:
                    # Display on the screen if debug
                    if enable_debug:
                        print(n)
                    # Write the line in the new file
                    with open("stabilized.bf", "a") as append:
                        append.write(n + "\n")
                # If there are some characters left, add them
                if remaining_characters_count != 0:
                    # Check the difference and then store the last digits in a variable
                    remaining_characters = line[-remaining_characters_count:]
                    # Write the remaining characters in the last line (shorter than 60)
                    with open("stabilized.bf", "a") as append:
                        append.write(remaining_characters + "\n")
                # Print those characters in the end of the output, if debug
                if enable_debug:
                    print(remaining_characters)
                    print()
                    print("^" + " " * (remaining_characters_count - 2) + "^")  # Mark the lenght. Just for the flex
                    print(" REMAINING CHARACTERS: " + str(remaining_characters_count))

main()
