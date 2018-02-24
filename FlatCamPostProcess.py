import re
import fileinput
p = re.compile('\A([GM])0(.)(.*)')

for line in fileinput.input(inplace=1,backup='.bak'):
    t = p.match(line)
    if t != None:
        foo = ''
        for i in t.groups():
            i = re.sub('([XYZ])', r' \1', i)
            foo += i
        ''' Debugging shows filment output in repetier
        if t.group(2) == '1':
            foo += ' E2' 
        '''
        print(foo)
    else:
        print line.strip()
