import sys, xml.etree.ElementTree, codecs

filename = sys.argv[1]
dafile = codecs.open(filename, 'r', 'latin1')
p = xml.etree.ElementTree.XMLParser(encoding='ISO-8859-1')
#p = xml.etree.ElementTree.XMLParser(encoding="UTF-8")
#et = xml.etree.ElementTree.parse(file, parser)
#two different xml parsers keep burping at the poorly-structured format of the doc


xml.etree.ElementTree.XML(dafile.read(), p)
exit()
#gets the next document element from 'file' as a string
#do not call in the middle of another document.
#returns an XML 'Element', or false if EOF
def getNextDocumentElement(myFile):
    eltString = ""
    line = myFile.readline()
     
    while(line != ""):  #while not eof
        eltString += line
        if line.strip() == "</doc>":
            break;  #exit loop if end of elt found
        else:
            line = myFile.readline()
    if eltString == "":
        return False
    else:
#        print eltString
        print str(p)
        return xml.etree.ElementTree.XML(eltString, p)

getNextDocumentElement(dafile)
documentID = ""
