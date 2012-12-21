import sys
import fileinput

for line in fileinput.input(sys.argv[1], inplace=True):
    if (line[0] == '<' and (line[:4] != '<doc' and line[:6] != '</doc>')) or line[0] == '>':
       print '<![CDATA[' + line[:-1] + ']]>\n',
    else:
        print line,
    
    
