import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_367896.xml'
my_xml = urllib.request.urlopen(url).read()

tree = ET.fromstring(my_xml)
counts = tree.findall('.//count')

def calsum(l): 
    # returning sum of list using List comprehension 
    return  sum([int(i.text) for i in l ])

print(calsum(counts))