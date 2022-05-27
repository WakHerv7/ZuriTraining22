# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):

    list_word = list(word)
    list_word.sort()

    list_anagram = list(anagram)
    list_anagram.sort()
    
    i = 0
  
    while i < len(word):  
        if list_word[i]==list_anagram[i]:  
            i = i + 1  
        else:
            return False
  
    return True


print(find_anagram("hello", "check"))
print(find_anagram("below", "elbow"))