f = open('newfile.txt', 'a')
lines = ['Hello','Welcome','To','File IO']
f.writelines(lines)
f.close()