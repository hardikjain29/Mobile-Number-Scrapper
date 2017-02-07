import os

for root, dirs, files in os.walk("."): #instead of . the directory of the text files,if in same folder(./folderName)
    path = root.split(os.sep)
    for file in files:
        f = open(file , 'r')
        for word in f.read().split():
    		if(word[0]=='+' and word[1]=='9' and word[2]=='1'): # To check if the number is Indian as 10 digit can also be from other country
    			req = word[3:]
    			if(req.isdigit() and len(req)==10):
    				print(req)
    		if(word[0]=='0' and word[1]=='0' and word[2]=='9' and word[3]=='1'):
    			req = word[4:]
    			if(req.isdigit() and len(req)==10):
    				print(req)
        f = open(file , 'r')
        for word in f.read().split():
            if(word.isdigit() and len(word)==10):
                print(word)