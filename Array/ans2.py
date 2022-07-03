heros=['spider man','thor','hulk','iron man','captain america']
#1 length of list
print(len(heros))
#2 Add 'black panther'
heros.append('black panther')
print(heros)
#3
heros.pop()
heros.insert(3,'black panther')
print(heros)
#4
heros[1]='doctor strange'
heros.pop(2)
#5
dir(heros)
print(heros.sort())



