'''Name:Asmita Hon
RollNo:71
Batch: B4
Program: Regular Expression in Python'''

import re

regex = (r"[A-Z]{5}[0-9]{4}[A-Z]{1}\n"
	r"\b\d{1,3}\.\d{1,3}\.\d{1,2}\.\d{1,1}\n"
	r"\d{1,2}\/\d{1,2}\/\d{2,4}\n"
	r"[A-z]{6}[A-z]{8}[A-z]{3}")

test_str = ("BCBPH8858M\n"
	"192.168.52.1\n"
	"22/11/2023\n"
	"AsmitaRaosahebHon")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

'''OUTPUT
 BCBPH8858M
192.168.52.1
22/11/2023
AsmitaRaosahebHon
Group 1 found at 0-5: BCBPH
Group 2 found at 5-9: 8858
Group 3 found at 9-10: M
Group 4 found at 11-14: 192
Group 5 found at 15-18: 168
Group 6 found at 19-21: 52
Group 7 found at 22-23: 1
Group 8 found at 35-41: Asmita
Group 9 found at 41-49: Raosaheb
Group 10 found at 49-52: Hon
BCBPH8858M
192.168.52.1
22/11/2023
AsmitaRaosahebHon
'''