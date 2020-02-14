# This function takes two strings and identifies the unique words and returns them. 
def UniqueWords(x, y): 
  
    # wordcount will calculate the word counts 
    wordcount = {} 
      
    # get word counts for string x
    for token in x.split(): 
        wordcount[token] = wordcount.get(token, 0) + 1
      
    # get wordcounts for string y 
    for token in y.split(): 
        wordcount[token] = wordcount.get(token, 0) + 1
  
    # return unique words
    return [token for token in wordcount if wordcount[token] == 1] 
  
# Driver Code 
string1 = "Lists, tuples, dictionaries and sets are various datastructures in Python"
string2 = "Files, arrays are datastructures in Python too"
  
# Print required answer 
print(UniqueWords(string1,string2))
