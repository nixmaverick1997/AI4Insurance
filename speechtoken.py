import nltk
import tscribe
import json
import csv
tscribe.write('C:\\Users\\nikhil.c.nair\\Documents\\AIHackathon\\ai-northstar.json',format="csv",save_as="transcript.csv")
with open(r'C:\Users\nikhil.c.nair\Documents\AIHackathon\transcript.txt', "w") as outputfile:
    with open(r'C:\Users\nikhil.c.nair\Documents\AIHackathon\transcript.csv', newline='') as myFile:
        reader = csv.DictReader(myFile)
        for row in reader:
            writer= outputfile.write(row['comment'])
f=open(r'C:\Users\nikhil.c.nair\Documents\AIHackathon\transcript.txt','r')
raw=f.read()
sentences=nltk.sent_tokenize(raw)
for sentence in sentences:
    print(sentence)
    print()
text = nltk.Text(sentences)
