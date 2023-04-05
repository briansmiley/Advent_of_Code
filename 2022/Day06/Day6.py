import os
cwd = os.getcwd()
file = open(cwd + "buffer.txt","r")
buffer = file.readlines()[0]
# buffer = "aabaabcdaaaaaaazxcvbnmasdfghjkl"
chunk = buffer[:3]
found = False
startsig = 0 
for idx, char in enumerate(buffer[3:]):
    chunk = chunk + char
    repeat = False
    for let in chunk:
        if chunk.count(let) > 1:
            repeat = True
            break
    if not(repeat):
        startsig = idx + 4
        break
    chunk = chunk[1:]
    

chunk = buffer[startsig:startsig+13]
startmessage = None
for idx, char in enumerate(buffer[startsig+13:]):
    repeat = False
    for let in chunk:
        if chunk.count(let) > 1:
            repeat = True
            break
    if not(repeat):
        startmessage = idx + startsig + 14
        break
    chunk = chunk[1:] + char

print("4 char message sig at: ",startsig,"\n14 char message start at: ",startmessage)

