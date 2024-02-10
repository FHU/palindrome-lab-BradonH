#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    word = word.replace(' ','')
    word = word.lower()
    backwards = []
    if len(word) <= 1:
        return False
    else:
        for i in range(0,len(word)):
            backwards.append(word[i])
        backwards.reverse()
        backwards = ''.join(backwards)
        if backwards == word:
            return True
        else:
            return False




#YOUR CODE GOES HERE\
if __name__ == '__main__':
    test_word = str(input())
    segment = ["1", "2", "3"]
    palindrome(test_word) 
#test
#test3