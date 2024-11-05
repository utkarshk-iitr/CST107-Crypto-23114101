We convert the upper case letters to numbers using ord function and then subtract 65 to make A = 0 , B = 1 ....

To convert back to letters we add 65 to it and then use chr function to convert back to upper case

To decrypt the messsage we first convert the upper case to numbers then we do a frequency analysis on the occurence we then predict that max occurence is of 'e'.
If the output found is correct then we end the program, else we do a exhaustive brute force search on the key and decrypt the ciphertext
