"""
winner word analyzer
"""

#function that loads a lexicon of positive words to a set and returns the set
def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname)
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex


negLex=loadLexicon('negative-words.txt')


file_writer=open('winner.txt','w')

data_conn=open('input.txt')
winner_words=dict()
max = 0
winner_word = ''
for line in data_conn: 
    posList=[] 
    negList=[] 
    bad_words=set()

    line=line.strip()    
    
    words=line.split(' ') 
    
    for word in words: #for every word in the review
        if word in negLex:
            bad_words.add(word)


    for word in bad_words:      
        if word in winner_words:
            winner_words[word] = winner_words[word] + 1
        else:
            winner_words[word] = 1

        if max < winner_words[word]:
            max = winner_words[word]
            winner_word = word

file_writer.write(winner_word)

file_writer.close()
data_conn.close()


