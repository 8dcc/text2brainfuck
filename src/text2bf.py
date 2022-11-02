# https://github.com/r4v10l1
# https://gist.github.com/r4v10l1/34a13e265b528c4975a719abed3d45a0
import sys, math

#######  EDIT ME  #########
debug = False             #  Boolean. Print in console extra stuff.
mode = "2"                #  Make sure you put the number inside a string!
match_paragraphs = False  #  If there is a \n in the input file, type a \n in the output.bf
###########################

def check_file_argv():
    if len(sys.argv) > 1:
        if sys.argv[1] == "-f":
            if len(sys.argv) > 2:
                return True
            else:
                error_exit("You specified the \'-f\' argument but you didn't specify a file!")
        else:
            error_exit("You need to specify \'-f\' in order to use the file mode!")
    else:
        return False

def clear_file(filename):
    with open(filename, "w") as clear_file:
        clear_file.write("[ Made using https://github.com/r4v0l1/text2brainfuck ]\n\n")

def error_exit(text):
    print()
    print(f" [!] {text}")
    exit(1)

def debug_func(a1, a2, a3, a4, a5, a6):
    if a1 == "\n":
        print("   ┌ Character: \\n")
    else:
        print(f"   ┌ Character: {a1}")
    print(f"   │ Ascii value: {a2}")
    print(f"   │ Value 1: {a3}")
    print(f"   │ Value 2: {int(a4)}")
    print(f"   │ BF Total: {int(a5)}")
    print(f"   └ BF Remaining: {int(a6)}")
    print()

# Mode 1. Using a memory block for each value.
def mode1(string2translate):
    for character in string2translate:
        ascii_value = int(ord(character))
        bf_plus_count_1 = int(math.sqrt(ascii_value))
        for i in range(2, 15):
            if ascii_value % i == 0:
                bf_plus_count_1 = i
        bf_plus_count_2 = ascii_value / bf_plus_count_1

        bf_total = int(bf_plus_count_1) * int(bf_plus_count_2)
        if ascii_value > bf_total:
            bf_remaining = ascii_value - bf_total
        else:
            bf_remaining = 0

        # Write into the bf script
        with open("output.bf", "a") as bf_file:
            # Add part 1 (mult. 1)
            bf_file.write(">" + "+" * bf_plus_count_1)
            # Add part 2 (mult. 2)
            bf_file.write("[<" + "+" * int(bf_plus_count_2) + ">-]<")
            # Add the extra characters
            if bf_remaining != 0:
                bf_file.write("+" * bf_remaining)
            # Print the character
            bf_file.write(".>")

        if debug:
            debug_func(character, ascii_value, bf_plus_count_1, int(bf_plus_count_2), int(bf_total), int(bf_remaining))

# Mode 2. Deleting value and writing the new one in the same memory block.
def mode2(string2translate):
    for character in string2translate:
        ascii_value = int(ord(character))
        bf_plus_count_1 = int(math.sqrt(ascii_value))
        for i in range(2, 15):
            if ascii_value % i == 0:
                bf_plus_count_1 = i
        bf_plus_count_2 = ascii_value / bf_plus_count_1

        bf_total = int(bf_plus_count_1) * int(bf_plus_count_2)
        if ascii_value > bf_total:
            bf_remaining = ascii_value - bf_total
        else:
            bf_remaining = 0

        with open("output.bf", "a") as bf_file:
            bf_file.write(">" + "+" * bf_plus_count_1)  # Part 1
            bf_file.write("[<" + "+" * int(bf_plus_count_2) + ">-]<")  # Part 2
            if bf_remaining != 0:
                bf_file.write("+" * bf_remaining)  # Add the remaining
            bf_file.write(".[-]")  # Print the character
            #  Instead of moving the memory block, delete until it's 0,
            #  then start to write the new character in that memory block.

        if debug:
            debug_func(character, ascii_value, bf_plus_count_1, int(bf_plus_count_2), int(bf_total), int(bf_remaining))

# Mode 3. Going from old value to new.
def mode3(string2translate):
    global old_ascii_value
    global first_time
    for character in string2translate:
        ascii_value = int(ord(character))
        if first_time:
            bf_plus_count_1 = int(math.sqrt(ascii_value))
            for i in range(2, 15):
                if ascii_value % i == 0:
                    bf_plus_count_1 = i
            bf_plus_count_2 = ascii_value / bf_plus_count_1
            bf_total = int(bf_plus_count_1) * int(bf_plus_count_2)
            if ascii_value > bf_total:
                bf_remaining = ascii_value - bf_total
            else:
                bf_remaining = 0
            with open("output.bf", "a") as bf_file:
                bf_file.write(">" + "+" * bf_plus_count_1)
                bf_file.write("[<" + "+" * int(bf_plus_count_2) + ">-]<")
                if bf_remaining != 0:
                    bf_file.write("+" * bf_remaining)
                bf_file.write(".")
            first_time = False

        else:
            # If we want to print the same value again
            if ascii_value == old_ascii_value:
                with open("output.bf", "a") as bf_file:
                    bf_file.write(".")

            # If we want to increase the value
            elif ascii_value > old_ascii_value:
                difference = ascii_value - old_ascii_value
                bf_plus_count_1 = int(math.sqrt(difference))
                for i in range(2, int(difference / 2)):
                    if difference % i == 0:
                        bf_plus_count_1 = i
                bf_plus_count_2 = difference / bf_plus_count_1
                bf_total = int(bf_plus_count_1) * int(bf_plus_count_2)
                if difference > bf_total:
                    bf_remaining = difference - bf_total
                else:
                    bf_remaining = 0

                with open("output.bf", "a") as bf_file:
                    bf_file.write(">" + "+" * bf_plus_count_1)
                    bf_file.write("[<" + "+" * int(bf_plus_count_2) + ">-]<")
                    if bf_remaining != 0:
                        bf_file.write("+" * bf_remaining)
                    bf_file.write(".")

            # If we want to decrease the value
            elif ascii_value < old_ascii_value:
                difference = old_ascii_value - ascii_value
                bf_plus_count_1 = int(math.sqrt(difference))
                for i in range(2, int(difference / 2)):
                    if difference % i == 0:
                        bf_plus_count_1 = i
                bf_plus_count_2 = difference / bf_plus_count_1
                bf_total = int(bf_plus_count_1) * int(bf_plus_count_2)
                if difference > bf_total:
                    bf_remaining = difference - bf_total
                else:
                    bf_remaining = 0

                with open("output.bf", "a") as bf_file:
                    bf_file.write(">" + "+" * bf_plus_count_1)
                    bf_file.write("[<" + "-" * int(bf_plus_count_2) + ">-]<")
                    if bf_remaining != 0:
                        bf_file.write("-" * bf_remaining)
                    bf_file.write(".")
            else:
                error_exit("Unknown error in mode 3. Exiting...")

        old_ascii_value = ascii_value
        if debug:
            debug_func(character, ascii_value, bf_plus_count_1, int(bf_plus_count_2), int(bf_total), int(bf_remaining))

def main():
    clear_file("output.bf")
    if check_file_argv():
        with open(sys.argv[2], "r") as input_file:  # Read the input file
            while True:
                line = input_file.readline()  # Read each line in a loop
                if not line:  # If there are no lines left exit the loop
                    break
                if mode == "1":
                    mode1(line)
                elif mode == "2":
                    mode2(line)
                elif mode == "3":
                    mode3(line)
                    first_time = False
                if match_paragraphs:
                    with open("output.bf", "a") as bf_file:
                        bf_file.write("\n\n")
    elif not check_file_argv():
        print()
        if mode == "1":
            mode1(input(" [?] String to translate: "))
            print()
        elif mode == "2":
            mode2(input(" [?] String to translate: "))
            print()
        elif mode == "3":
            mode3(input(" [?] String to translate: "))
            print()
            first_time = False

first_time = True  # Don't touch this
main()
