import re
 
      
def chainNumerical( str ):
    smile = str
    pattern1 = r':[0-9]+'
    smile = re.sub(pattern1, '', smile)
    pattern2 = '[A-Z]'
    smile = re.sub(pattern2, lambda x: ' '+x.group(0), smile)
    pattern3 = '[0-9]'
    smile = re.sub(pattern3, lambda x: ' '+x.group(0),smile)
    
    return smile
        
        
if __name__ == '__main__':
    s1 = r'Cl'
    s2 = r'CBaVi[OH:2][C@@H:3]|[CH:4]=[CH:5][CH:6]1[CH2:10][CH2:9][C:8]|[CH:7]1[CH2:12][CH:13]=[CH:14][CH2:15][CH2:16][CH2:17][C:18]|=[O:19]'
    s3 = r'C(O)C'
    s4 = ['[CH2:21][CH2:22][CH2:23][CH2:24][CH3:25]', '=[O:11]', '[OH:20]']
    s5 = r'_____(_____)_=__1___(=_)_1__=_____(_)=_' 
    print(chainNumerical(s1))
    print(chainNumerical(s2))    
        
        
