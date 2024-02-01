#Bryna Stern
#This program accepts a string from the user, replaces all numbers between 0 and 99 with their text equivalent, and returns the string

#Define the main method
def main():

    # The user is prompted to enter a string
    userString = input("Enter an input string: ")

    # Get the result of the string after the numbers have been replaced with text versions
    stringAfterChanges = replaceNumbersForTextEquivalent(userString)

    # Display the final string
    print(stringAfterChanges)

#This method defines the text eqivalent of numbers between 0 and 99
#and returns the text equivalent for the number passed in as a parameter
def textEquivalentOfNumbers(number):

    # The numbers 0 to 99 are divided into 2 lists: the zeroToNineteen list and the tens list
    zeroToNineteen = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                      "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
                      "eighteen", "nineteen"]
    #The first 2 elements are empty strings, since 0 and 10 are defined in the zeroToNineteen list
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    #If the number passed into this method is between 0 and 19, a word from the zeroToNineteen list is returned
    if 0 <= number <= 19:
        return zeroToNineteen[number]
        
    #If the number passed into this method is between 20 and 99, the following logic is implemented: 
    elif 20 <= number <= 99:
        
        #Check if the ones place is zero by calculating whether the number has a remainder after dividing the number by 10
        if number % 10 == 0:
            
            #If the ones place is 0, then just return a word from the tens list
            return tens[number // 10]
            
        #If the ones place is not zero, then return a word from both the tens list and the zeroToNineteen list, with a space in between
        else:
            return tens[number // 10] + " " + zeroToNineteen[number % 10]

#This method replaces the numbers with their text equivalents.
#This method receives the user's string as a parameter
def replaceNumbersForTextEquivalent(userString):
    
    #Split the user's string into words
    words = userString.split()

    #Go through each word in the list of words from the user's input
    for i in range(len(words)):
    
        #Check if the word is a number (isdigit()) and is between 0 and 99
        if words[i].isdigit() and 0 <= int(words[i]) <= 99:
        
            #Replace the number with its text equivalent
            words[i] = textEquivalentOfNumbers(int(words[i]))

    #Join the words back into a string, separating the words with a space
    stringAfterChanges = " ".join(words)
    
    #Return the string, after all necessary replacements have occurred
    return stringAfterChanges

#Call the main method
main()
