# CMSI-583(Computation and Complexity) - Final Project

## Implemention of Turing Machine in Python
In collaboration with:
[@ Nasim](https://github.com/snalahi)

**Students**
1. Kanimozhi Kanagaraj
2. Sk Nasimul Alahi

## Project Description: 
A Turing Machine consists of three parts: tape, write head, machine state. Tape is divided into sequences of squares. Each square may store a character or may be blank for a given character set.
The algorithm used for implementation using a Turing machine formal definition:

A deterministic Turing machine can be defined as a 7-tuple
* M = (Q, Σ, Γ, δ, q0, qaccept, qreject), where Q, Σ, Γ are all finite sets and
    - Q - set of states 
    - Σ - is the input alphabet not containing a blank symbol ⊔ 
    - Γ - is the tape alphabet, where `⊔ ∈ Γ and Σ ⊆ Γ 
    - δ - Q × Γ→ Q × Γ × {L,R} is the transition function. 
    - q0 ∈ Q is the start state 
    - qaccept ∈ Q is the accept state and 
    - qreject ∈ Q is the reject state, where qreject ≠ qaccept

For this project we implemented a Turing Machine that takes in binary numbers in python that performs any functions based on rules(under functions folder) and tapes(under tapes folder) provided via text file . The following are the functions we used in our project:
1. Increment
2. Decremnet
3. complement
4. Palindrome checker
5. Divisible by 3

The turing machine provides if given strings are accepted or not accepted.

## Program Description

1. turing_machine.py : This performs the complete turing machine function. Each function decription is mention as comments in the program
2. main.py : Read the functions and tapes files

## Running the program 

### commmand to run the program is : 
   ### For Complement 
    ``` python main.py -f Complement -t Complement ```
   ### For Increment
     ``` python main.py -f Increment -t Increment ```
   ### For Decrement
     ``` python main.py -f Decrement -t Decrement ```
   ### For Palindrome
    ``` python main.py -f Palindrome -t Palindrome ``` 
   ### For Divisible by three
    ``` python main.py -f Divbythree -t Divbythree ```

## Function format
    ```
    Complementstart 0 Complementstart 1 right
    Complementstart 1 Complementstart 0 right
    Complementstart b Complementone b left

    Complementone 0 Complementone 0 left
    Complementone 1 Complementone 1 left
    Complementone b Complementfinal b right

    ```
## working of the function
When describing the function, we map the states and their inputs to a Python dict. This allows us to transition through the table quickly.

```
Here is the map of the Complement function above
{
    "Complement" : {
        "0" : {
            "next": "Complementstart",
            "write": "1",
            "direction" : "right"
        },
        "1": {
            "next": "Complementstart",
            "write": "0",
            "direction" : "right"
        },
        "b": {
            "next": "Complementone",
            "write": "b",
            "direction" : "left"
        }
    },
    "Complementone" : {
        "0" : {
            "next": "Complementone",
            "write": "0",
            "direction" : "left"
        },
        "1": {
            "next": "complementone",
            "write": "1",
            "direction" : "left"
        },
        "b": {
            "next": "Complementfinal",
            "write": "b",
            "direction" : "right"
        }
    }
}
```

## Tape format

Tapes must me of this format
```
b1111111111111111111111b
b00000000000000000000000000000000bb
b10111001111100011011010010011000001101101bbb
b100011011110001111000110111011011bb
b011110001111111111010110101111111010101b
b00000000000000011111111111111110000000b

```

Notice the leading 'b', this signifies a blank on the tape. The Turing Machine will automatically position itself over the starting position, the leftmost non-blank. Although traditional turing machines can have an arbitrary number of blanks to the left, in accordance with the guidelines of this project, all input strings must have exactly one leading and ending blank, 'b'.

## Description of functions

1. Complement
    - The input string of 0 and 1 symbols is treated as a
    binary number. The TM should write the **complement** in place
    of the number presented as input on the TM tape. Since this is a core
    subprogram to be used for other arithmetic, the TM should not finish
    and accept until the tape head is positioned once again on the leftmost
    non-blank character of the input string
    
    - **command to run the complement is  :** ``` python main.py -f Complement -t Complement ```

2. Increment
    - The input string of 0 and 1 symbols is treated as a binary
    number n in backwards order from the usual way in which numbers
    are written. That is, the number is to be read left to right instead of
    right to left. The TM should increment the number by 1 so that it is
    now the binary number that is n + 1. Since this is a core subprogram
    to be used for other arithmetic, the TM should not finish and accept
    until the tape head is positioned once again on the leftmost non-blank
    character of the input string.
    
    - **command to run the Increment is  :** ``` python main.py -f Increment -t Increment ```

3. Decrement
    - The input string of 0 and 1 symbols is treated as a binary
    number n in backwards order from the usual way in which numbers
    are written. That is, the number is to be read left to right instead of
    right to left. The TM should decrement the number by 1 so that it is
    now the binary number that is n − 1. Note that decrementing, that is,
    subtracting 1, can be done by doing a ones’ complement, an increment,
    and a ones’ complement. Since this is a core subprogram to be used for
    other arithmetic, the TM should not finish and accept until the tape
    head is positioned once again on the leftmost non-blank character of
    the input string
    - **command to run the Decrement is  :** ``` python main.py -f Decrement -t Decrement ```        


4. Palindromes
    - The input string of 0 and 1 symbols is tested
    to see if it is a palindrome. If it is, the TM halts and accepts. If it is
    not, the TM halts without accepting.

    - **command to run the Palindrome is  :** ``` python main.py -f Palindrome -t Palindrome ```      

5. Divisible by three
    - The input string of 0 and 1 symbols is treated as a binary
    number n, written in left-to-right order. The TM should determine if n
    is a multiple of 3. If so, it should halt and accept. If not, it should halt
    without accepting. Note that this can be done by subtracting 3 (binary 11) from the input number, moving right to left and subtracting if the
    bit is a 1. If this process results in 0, then n is divisible by 3. If it does
    not result in 0, then n is not divisible by 3

    - **command to run the Divisible by three is  :** ``` python main.py -f Divbythree -t Divbythree ```      


we used the argparse module as it makes easy to write user-friendly command-line interfaces.

Here in our project - 
    -f FUNCTION, The name of the function, **also defines the prefix for all states**
    -t TAPE,  File name of the tape.

command line to view the what each parser means 
```
python3 main.py -h -f FUNCTION -t TAPE

```
