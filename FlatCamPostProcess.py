import re
import fileinput
p = re.compile('\A([GM])0(.)(.*)')

for line in fileinput.input(inplace=0,backup='.bak'):
    t = p.match(line)
    if t != None:
        foo = ''
        for i in t.groups():
            i = re.sub('([XYZ])', r' \1', i)
            foo += i
        
        if t.group(2) == '1':
            foo += ' E2'
        print(foo)
    else:
        print line.strip()
