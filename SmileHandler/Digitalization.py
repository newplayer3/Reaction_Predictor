import re
from parameter import smileInfo as SI
 
      
def atomnNumerical( str ):
    smile = str
    pattern1 = r'[A-Z][a-z]*'
    atoms = re.findall(pattern1, smile)
    digiAtom = []
    for atom in atoms:
        digiAtom.append(SI.smileInfo[atom].value)
    return digiAtom     
    
        

    

        
        
if __name__ == '__main__':
    s1 = r'Cl'
    s2 = r'[OH:2][C@@H:3]|[CH:4]=[CH:5][CH:6]1[CH2:10][CH2:9][C:8]|[CH:7]1[CH2:12][CH:13]=[CH:14][CH2:15][CH2:16][CH2:17][C:18]|=[O:19]'
    s3 = r'C(O)C'
    s4 = ['[CH2:21][CH2:22][CH2:23][CH2:24][CH3:25]', '=[O:11]', '[OH:20]']
    s5 = r'_____(_____)_=__1___(=_)_1__=_____(_)=_' 
    print(atomnNumerical(s2))
        
        
