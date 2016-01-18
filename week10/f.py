content=open('in.txt')
filewriter=open('out.txt','w')
for sentence in content:
    words=sentence.split(' ')
    sentence_after=''
    for word in words:
        if word.lower()=='not':
            sentence_after=sentence_after+word
        else:
            sentence_after=sentence_after+word+' '
    filewriter.write(sentence_after.strip()+'\n')
filewriter.close()
