import re
import fileinput
#p = re.compile('\A([GM])0(.)(.*)')
p = re.compile('\A(G1 [XYZ].*[S])(.\.\d*)+?( F.*)?')
p2 = re.compile('\A([XYZ].*)')    
for line in fileinput.input(inplace=1,backup='.bak'):
    t = p2.match(line)
    if t != None:
        foo = 'G1 '
        foo += t.group(1)
        line = foo
    m = p.match(line)
    if m != None:
        foo = ''
        foo += m.group(1)
        foo += str(int(round(float(m.group(2)) * 255)))
        if m.group(3) != None:
            foo += ' '
            foo += m.group(3).strip()
        ''' Debugging shows filment output in repetier
        if t.group(2) == '1':
            foo += ' E2' 
        '''
        #print(line.strip())
        print(foo)
    else:
        
        print line.strip()
