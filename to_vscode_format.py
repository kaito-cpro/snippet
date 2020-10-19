import re

f = open('hoge.cpp', 'r')
text = f.read()
f.close()

text = re.sub(r'"', r'\"', text)

f = open('hoge_new.cpp', 'w')
for line in text.split('\n'):
    f.write("\"" + line + "\",\n")
f.close()
