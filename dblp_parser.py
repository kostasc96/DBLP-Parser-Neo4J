import gzip
from lxml import etree
from xml.etree.ElementTree import ParseError
from lxml.etree import XMLSyntaxError
import re

parser = etree.XMLParser(load_dtd=True)

dtd = '<!DOCTYPE dblp SYSTEM "dblp.dtd">'


def parser_articles(file_name, dtd1, num1):
    i=0
    writing = False
    start = "<article"
    end = "</article>"
    regexp1 = "</article><[^A-Z]+"
    dtd = dtd1
    xml = dtd
    with gzip.open(file_name,'rt') as f:
        for line in f:
            try:
                if i > num1:
                    break
                #print(str(i) + ": " + line)
                if end in line:
                    index = line.find(end) + len(end)
                    xml += line[:index]
                    try:
                        xmldoc = etree.fromstring(xml, parser=parser)
                    except XMLSyntaxError:
                        xml = dtd
                        writing = False 
                        if start in line:
                            writing = True
                            index = line.find(start)
                            xml += line[index:]
                        continue
                    title = xmldoc.find(".//title").text
                    year = xmldoc.find(".//year").text
                    journal = xmldoc.find(".//journal").text
                    authors = []
                    if title:
                        for author in xmldoc.findall(".//author"):
                            authors.append(author.text)
                    if(title == None or year == None or journal == None or len(authors) == 0):
                        if start in line:
                            writing = True
                            index = line.find(start)
                            xml += line[index:]
                        continue
                    i+=1
                    print("Article")
                    #print(str(i) + "\n" + "title: " + title)
                    print(str(i) + " \n" + "title:" + title + " \n" + "year:" + year + " \n" + "journal:" +journal)
                    for author in authors:
                        print(author)
                    print("--------------------------------")
                    xml = dtd
                    writing = False

                if start in line:
                    writing = True
                    index = line.find(start)
                    xml += line[index:]
                elif writing:
                    xml += line
            except ParseError:
                xml = dtd
                continue



def parser_inproceedings(file_name, dtd1, num1):
    i=0
    writing = False
    start2 = "<inproceedings"
    end2 = "</inproceedings>"
    regexp2 = "</inproceedings><[^A-Z]+"
    pattern1 = "[0-9]+-"
    pattern2 = "-[0-9]+"
    dtd = dtd1
    xml = dtd
    with gzip.open(file_name,'rt') as f:
        for line in f:
            try:
                if i > num1:
                    break
                #print(str(i) + ": " + line)
                if end2 in line:
                    index2 = line.find(end2) + len(end2)
                    xml += line[:index2]
                    try:
                        xmldoc = etree.fromstring(xml, parser=parser)
                    except XMLSyntaxError:
                        xml = dtd
                        writing = False 
                        if start2 in line:
                            writing = True
                            index2 = line.find(start2)
                            xml += line[index2:]
                        continue
                    title = xmldoc.find(".//title").text
                    year = xmldoc.find(".//year").text
                    booktitle = xmldoc.find(".//booktitle").text
                    pages = ""
                    pageFrom = ""
                    pageTo = ""
                    numOfPages = 1
                    if re.search("<pages>.*[0-9]+-[0-9]+.*</pages>", str(xml)):
                        pages = re.search("<pages>.*[0-9]+-[0-9]+.*</pages>", str(xml)).group(0).replace('<pages>','').replace('</pages>','')
                        pages = re.search("[0-9]+-[0-9]+", pages).group(0)
                        pageFrom = re.search(pattern1, pages).group(0).replace('-','')
                        pageTo = re.search(pattern2, pages).group(0).replace('-','')
                        numOfPages = int(float(pageTo)) - int(float(pageFrom)) + 1
                    authors = []
                    if title:
                        for author in xmldoc.findall(".//author"):
                            authors.append(author.text)
                    if(title == None or year == None or booktitle == None or len(authors) == 0):
                        if start2 in line:
                            writing = True
                            index2 = line.find(start2)
                            xml += line[index2:]
                        continue
                    i+=1
                    print("Inproceeding")
                    print(str(i) + " \n" + "title:" + title + " \n" + "year:" + year + " \n" + "booktitle:" +booktitle + "\n" + "numOfPages:" + str(numOfPages))
                    for author in authors:
                        print(author)
                    print("--------------------------------")
                    xml = dtd
                    writing = False
                
                if start2 in line:
                    writing = True
                    index2 = line.find(start2)
                    xml += line[index2:]
                elif writing:
                    xml += line
            except ParseError:
                xml = dtd
                continue



def parser_incollections(file_name, dtd1, num1):
    i=0
    writing = False
    start3 = "<incollection"
    end3 = "</incollection>"
    regexp3 = "</incollection><[^A-Z]+"
    pattern1 = "[0-9]+-"
    pattern2 = "-[0-9]+"
    dtd = dtd1
    xml = dtd
    with gzip.open(file_name,'rt') as f:
        for line in f:
            try:
                if i > num1:
                    break
                #print(str(i) + ": " + line)
                if end3 in line:
                    index3 = line.find(end3) + len(end3)
                    xml += line[:index3]
                    try:
                        xmldoc = etree.fromstring(xml, parser=parser)
                    except XMLSyntaxError:
                        xml = dtd
                        writing = False 
                        if start3 in line:
                            writing = True
                            index3 = line.find(start3)
                            xml += line[index3:]
                        continue
                    title = xmldoc.find(".//title").text
                    year = xmldoc.find(".//year").text
                    booktitle = xmldoc.find(".//booktitle").text
                    pages = ""
                    pageFrom = ""
                    pageTo = ""
                    numOfPages = 1
                    if re.search("<pages>.*[0-9]+-[0-9]+.*</pages>", str(xml)):
                        pages = re.search("<pages>.*[0-9]+-[0-9]+.*</pages>", str(xml)).group(0).replace('<pages>','').replace('</pages>','')
                        pages = re.search("[0-9]+-[0-9]+", pages).group(0)
                        pageFrom = re.search(pattern1, pages).group(0).replace('-','')
                        pageTo = re.search(pattern2, pages).group(0).replace('-','')
                        numOfPages = int(float(pageTo)) - int(float(pageFrom)) + 1
                    authors = []
                    if title:
                        for author in xmldoc.findall(".//author"):
                            authors.append(author.text)
                    if(title == None or year == None or booktitle == None or len(authors) == 0):
                        if start3 in line:
                            writing = True
                            index3 = line.find(start3)
                            xml += line[index3:]
                        continue
                    i+=1
                    print("Incollection")
                    print(str(i) + " \n" + "title:" + title + " \n" + "year:" + year + " \n" + "booktitle:" +booktitle + "\n" + "numOfPages:" + str(numOfPages))
                    for author in authors:
                        print(author)
                    print("--------------------------------")
                    xml = dtd
                    writing = False

                if start3 in line:
                    writing = True
                    index3 = line.find(start3)
                    xml += line[index3:]
                elif writing:
                    xml += line
            except ParseError:
                xml = dtd
                continue


parser_articles('dblp.xml.gz',dtd,1000)
#parser_inproceedings('dblp.xml.gz',dtd,1000)
#parser_incollections('dblp.xml.gz',dtd,1000)
