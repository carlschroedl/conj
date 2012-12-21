import sys
import fileinput

for line in fileinput.input(sys.argv[1], inplace=True):
    if '&' in line:
        line = line.replace('&', 'and')
    if (line[0] == '<' and line[:4] == '<doc'):
        # if there's more than 10 quotation marks, there are extra in the title
        if line.count('"') > 10:
            # get the beginning index of the title
            begin = line.find('title=') + 7
            # get the ending index of the title
            end = line.find('nonfiltered=') - 2
            # split the string into beginning, middle and end
            b = line[:begin]
            m = line[begin:end]
            e = line[end:]
            
            # remove the quotes from the title string
            m = m.replace('"', '')
            
            # reconstruct the new string
            line = b + m + e
            
        print line,
    elif (line[0] == '<' and line[:6] == '</doc>'):
         print line,
    elif (line[0] == '<' and line[:4] != '<doc') and (line[0] == '<' and line[:6] != '</doc>'):
         print '<![CDATA[' + line[:-1] + ']]>\n',
    elif line[0] == '>':
         print '<![CDATA[' + line[:-1] + ']]>\n',
    else:
         print line,
    
    
