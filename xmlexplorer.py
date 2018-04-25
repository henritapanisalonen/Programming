import urllib.request
import http.cookiejar
import xml.etree.ElementTree as ET

cj = http.cookiejar.MozillaCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
opener.addheaders = [("User-agent", "Mozilla/5.0")]

weburl = "http://clinicaltrials.gov/ct2/show/NCT01396239?displayxml=true"

try:
    infile = opener.open(weburl,timeout = 3)
    newpage = infile.read().decode("utf-8")
except:
    print("Page not found.")
    newfile = ""

root = ET.fromstring(newpage)
    
print(root.tag)
print(root.attrib)
print(root.text)
print()
print(root[0].tag)
print(root[1].tag)
print()

for child in root:
    print(child.tag,child.text)

titleelement = root.find("brief_title")
print("Brief title =",titleelement.text)

primaryoutcomeelement = root.find("primary_outcome")
for child in primaryoutcomeelement:
    print(child.text)
print()

secondaryoutcomelist = root.findall("secondary_outcome")
for secondaryoutcome in secondaryoutcomelist:
    for child in secondaryoutcome:
        print(child.text)
        print()
print()
