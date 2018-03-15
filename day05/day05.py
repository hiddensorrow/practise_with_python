import os
wordcount = 0

if os.path.exists('51060'):
    with open('51060', 'r') as f:
        for line in f:
            wordcount += len(line.split())
    print(wordcount)
else:
    print(wordcount)