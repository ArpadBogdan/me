"""
Commenting skills:

NOTE: this file runs just fine, this is for you to learn to use the debugger!

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ["what", "does", "this", "line", "do", "?"] #defines a list called some_words

for word in some_words: #it makes a for loop and makes it print off all the contents of some_words one line at a time until there isn't anything else to print
    print(word)

for x in some_words: #it makes a for loop and makes it print off all the contents of some_words one line at a time until there isn't anything else to print
    print(x)

print(some_words) #prints out the contents of some_words as they are stored

if len(some_words) > 3: #it esentially checks if there are more then 3 words in some_words and then prints them of if there are more then 3 words
    print("some_words contains more than 3 words")


def usefulFunction(): #it defiens a function and withing it, it prints of uname, which from research is a method to find general system information about the particula computer which you are executing the code on
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())


usefulFunction()
