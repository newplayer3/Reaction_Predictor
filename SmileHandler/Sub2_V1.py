# import atominfo as af
import re

class Sub2_V1:
    
    
    def __init__(self, str):
        self._smile = str
        self._molecule=[]
        
        self._setMolecule()
        
    def _setMolecule (self):
        self._molecule = self._smile.split('.')
    
    def getMolecule(self):
        return self._molecule


    
    
    
    
    

if __name__ == '__main__':
    s1 = r'Cl'
    s2 = r'CBaVi[OH:2][C@@H:3]|[CH:4]=[CH:5][CH:6]1[CH2:10][CH2:9][C:8]|[CH:7]1[CH2:12][CH:13]=[CH:14][CH2:15][CH2:16][CH2:17][C:18]|=[O:19]'

