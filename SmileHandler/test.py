import re
 
s1 = r'Cl.[OH:2][C@@H:3]([CH2:21][CH2:22][CH2:23][CH2:24][CH3:25])[CH:4]=[CH:5][CH:6]1[CH:10]=[CH:9][C:8](=[O:11])[CH:7]1[CH2:12][CH:13]=[CH:14][CH2:15][CH2:16][CH2:17][C:18]([OH:20])=[O:19]>C(O)C>[OH:2][C@@H:3]([CH2:21][CH2:22][CH2:23][CH2:24][CH3:25])[CH:4]=[CH:5][CH:6]1[CH2:10][CH2:9][C:8](=[O:11])[CH:7]1[CH2:12][CH:13]=[CH:14][CH2:15][CH2:16][CH2:17][C:18]([OH:20])=[O:19]'
 
pattern = re.compile(r'[A-Z][a-z]*')
f = re.findall(pattern, s1) 

print(f)

 