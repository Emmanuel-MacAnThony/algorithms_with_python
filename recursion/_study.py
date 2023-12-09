from typing import Set, Iterable

def cummulative(n: int):
    
    if n == 0:
        return 0
    else:
        return n + cummulative(n - 1)
    

def sum_func(n: int):
    
    numstr = str(n)
    
    if len(numstr) == 1:
        return n
    else:
        return int(numstr[0]) + sum_func(int(numstr[1:]))
    
def word_split(phrase: str, list_of_words: Set[str], output=None):
    
    if (len(list_of_words) == 0):
        if (len(phrase) == 0):
            return output
        else:
            return []
        
    else:
        
        startIndex = phrase.find(list_of_words[0])
        
        if startIndex:
            phrase = phrase[0: startIndex] + phrase[len(list_of_words[0]) + startIndex:]
            if output == None:
                output = []
            output = [list_of_words[0]] + output
      
        
        return [] + word_split(phrase, list_of_words[1:], output)
    
def double_array(array: Iterable, index:int):
    
    if index >= len(array):
        return;
    
    else:
        array[index] = array[index] * array[index]
        double_array(array, index + 1)
        
def reverse(string: str):
    
    if len(string) == 1:
        return string[0]
    
    return string[len(string) - 1] + reverse(string[:len(string) - 1])

ans = reverse('abcde')
print(ans)