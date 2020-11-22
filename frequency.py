import string
inp=input('Enter a file name: ')
fhand = open(inp)
count=dict()
rel_list = list()
for line in fhand:
    line=line.lower()
    line=line.translate(str.maketrans(' ',' ',string.punctuation))
    line=line.translate(str.maketrans(' ',' ',string.whitespace))
    line=line.translate(str.maketrans(' ',' ',string.digits))
    for words in line:
        for char in words:
            count[char]=count.get(char,0)+1
# print(count) 
for key,val in list(count.items()):
    rel_list.append((val,key))
rel_list.sort(reverse=True)

for val,key in rel_list:
    print(key,val)
