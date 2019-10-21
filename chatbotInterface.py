import giphy
import googleModel
text = ""
print("Welcome: I am the giphy robot using Google's NLP")

import pandas
df = pandas.read_excel('slang.xlsx')
#print the column names
values = df.columns

import re


#get a data frame with selected columns
FORMAT = values
df_selected = df[FORMAT]

while True:
    
    txt = input()
    if txt.lower() == "q" or txt.lower() == "quit":
        print()
        print("buh byeeeee")
        break
    lst = df.values.tolist()
    output = []
    for word in lst:
        if word[0] in txt.split():
            pattern = re.compile(word[0], re.IGNORECASE)
            txt = pattern.sub(word[1], txt)
            output.append([word[2],5]) 
    
    x = googleModel.sample_analyze_entities(txt)
    if x != []:
        output += x
    seen = []
    i = 0
    while i < 5 and i < len(output):
        if output[i][0] not in seen:
            giphy.gifGenerator(output[i][0], 2)
            seen.append(output[i][0]) 
            print(output[i][0])           
        i+=1

