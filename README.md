# Text to brainfuck
Python script for transforming text into brainfuck.
I had a look at brainfuck this morning and I decided to write this script in python.

I spent way too much time on this shit, enjoy being edgy.

## Installing

```bash
git clone https://github.com/r4v10l1/text2brainfuck
cd text2brainfuck
python text2bf.py [-f file.txt]
```

## Configuration
You can edit this 3 variables, I might add an argument for them or something.

#### Debug
```python
debug = False
```
Boolean. If set to true, it will display information about each character on the screen. See [How it works](https://github.com/r4v10l1/text2brainfuck/blob/main/README.md#how-it-works)
#### Mode
```python
mode = "3"
```
String. It is important to write the ```" "```.

There are 3 modes:
* **Mode one**: Will use a memory block for each character, and the next one as auxiliar when writing.
* **Mode two**: Will write in the first block, and use the next one as auxiliar. After printing the final number, it will subtract 1 until the block is empty. Then it will begin to write the next value in the same block, using the second as auxiliar like it did in the previous value.
* **Mode three**: Will use mode one for the first value, then it will check if the new value is bigger, smaller or the same as the old one. Depending on that, it will increase the old block value, reduce the old value until it reaches the new one, or it will print the value again, if it is the same.

#### Match paragraphs
```python
match_paragraphs = False
```
Boolean. If set to false, it will write the output as one line, even if there is more than one line in the input file.

If set to false, it will add ```\n\n``` (an empty line) between the paragraphs when writing the output file.

## How it works

See this for more detail: https://gist.github.com/r4v10l1/34a13e265b528c4975a719abed3d45a0

Example:

```
   ┌ Character: a
   │ Ascii value: 97
   │ Value 1: 9
   │ Value 2: 10
   │ BF Total: 90
   └ BF Remaining: 7
```
In this example, what brainfuck will do is add to the current memory block the ```Value 1``` in a loop that will execute ```Value 2``` times.

In order to know how many times it needs to add ```Value 1```, we store that (```Value 2```) in the next block (What I've been calling auxiliar).

If the ```Ascii value``` is not ```Value 1``` * ```Value 2```, it will store the difference in ```BF Remaining```, and then add it to the memory block.
