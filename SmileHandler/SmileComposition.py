# import atominfo as af
import re

class SmileComposition:
    
    
    def __init__(self, str):
        self._smile = str
        self._sidechain = ''
        self._mainchain = ''
        self._connection = ''
        
        self._setSideChain()
        self._setMainChain()
        self._setConnection()
    
    
    def _setSideChain(self):   #find all sideChain
        smile = self._smile
        pattern1 = re.compile(r'[(](.*?)[)]', re.S)       #regExp  [(] = (; (.*?) = recording every string untile meet the first ; [)] = ); re.S = ignore '/n'
        self._sidechain = re.findall(pattern1, smile)
        
    def _setMainChain(self):
        smile = self._smile
        pattern1 = re.compile(r'[(](.*?)[)]', re.S)
        smile = re.sub(pattern1, r'|', smile)
        self._mainchain = smile
    
    def _setConnection(self):
        smile = self._smile
        pattern1 = re.compile(r'\[(.*?)\]', re.S)
        pattern2 = re.compile(r'[A-Z][a-z]', re.S)
        pattern3 = re.compile(r'[A-Z]', re.S)
        smile = re.sub(pattern1, r'_', smile)
        smile = re.sub(pattern2, r'_', smile)
        smile = re.sub(pattern3, r'_', smile)    
        self._connection = smile      
                
    def getSideChain(self):
        return self._sidechain  
        
    def getMainChain(self):
        return self._mainchain    
    
    def getConnection(self):
        return self._connection
    
    
    
    
    
    

if __name__ == '__main__':
    s1 = r'Cl'
    s2 = r'CBaVi[OH:2][C@@H:3]|[CH:4]=[CH:5][CH:6]1[CH2:10][CH2:9][C:8]|[CH:7]1[CH2:12][CH:13]=[CH:14][CH2:15][CH2:16][CH2:17][C:18]|=[O:19]'
    s3 = r'C(O)C'
    s4 = ['[CH2:21][CH2:22][CH2:23][CH2:24][CH3:25]', '=[O:11]', '[OH:20]']
    s5 = r'_____(_____)_=__1___(=_)_1__=_____(_)=_'
    S = SmileComposition(s4)
    print(S.getMainChain())
    print(S.getSideChain())
    print(S.getConnection())

