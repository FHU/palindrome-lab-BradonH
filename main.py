#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
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




#YOUR CODE GOES HERE
test_word = str(input())
test_word = test_word.strip()
segment = ["1", "2", "3"]
palindrome(test_word) 

