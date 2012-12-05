import sys
import xml.etree.ElementTree as ET
import codecs

#import parser settings:
from parserConfig import ENCODING, ROOT_ELT_NAME, ROOT_START_TAG, ROOT_END_TAG, CORRECTED_FILENAME_PREFIX

filename = sys.argv[1]

#

#<correct missing root node>

file = codecs.open(filename, 'r', ENCODING)
firstline = file.readline().strip()

if firstline != ROOT_START_TAG:
    filename = CORRECTED_FILENAME_PREFIX + filename
    
    print "No root xml element detected. Correcting and writing to:"
    print filename
    print "..."
    
    newFile = codecs.open(filename, 'w', ENCODING)
    newFile.write(ROOT_START_TAG + "\n")

    file.seek(0) #rewind to beginning of file
    newFile.write(file.read()) #write old into new
    file.close()
    newFile.write(ROOT_END_TAG + "\n")
    newFile.close()

    print "Finished writing to" ,filename, "."
    print filename, "will now be parsed."


#</correct missing root node>

#<parse the valid xml doc>

#for docs on XMLParser
#@see: http://docs.python.org/2/library/xml.etree.elementtree.html#module-xml.etree.ElementTree

parser = ET.XMLParser(encoding=ENCODING)
et = ET.parse(filename, parser)
root = et.getroot()
docs = root.findall('doc')
for doc in docs:
    
    #doc.attrib is a dictionary of xml attribute names and values
    print "Document ID:", doc.attrib['id'] 
    
    #print doc.text 

    #line-by-line processing of the element text goes here

exit()


#<parse the valid xml doc>
















# @deprecated
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
