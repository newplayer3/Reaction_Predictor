#divide the string into different parts


class RecationSmile:
    
    
    
    def __init__(self, str):   
        self._input = str
        self._recationsmile =''
        self._reactants = []
        self._products = []
        self._agents = []
        
        
        self._setReactionSmile()
        self._setRactionComp()

   
    def _setReactionSmile(self):     #checking smile string have 2 > to represent a reaction
        if self._input.count(r'>') == 2:
            self._reactionsmile = self._input
        else:
            raise ValueError("smile string missing reacatant/catalyst/product ")
            
    
    def _setRactionComp(self):    # set reaction components
        smile = self._reactionsmile
        reactants = smile.split(r'>')[0]
        self._reactants = reactants.split('.')
        
        agents = smile.split(r'>')[1]
        self._agents = agents.split('.')
        
        products = smile.split(r'>')[2]
        self._products = products.split('.')
        
        
        
    def getRactants(self):
        return self._reactants
    
    def getProducts(self):
        return self._products
    
    def getAgents(self):
        return self._agents
    
    def getReactionSmile(self):
        return self._recationsmile
    
    
        
        
if __name__ == '__main__':
    s1 = r'Cl.[OH:2][C@@H:3]([CH2:21][CH2:22][CH2:23][CH2:24][CH3:25])[CH:4]=[CH:5][CH:6]1[CH:10]=[CH:9][C:8](=[O:11])[CH:7]1[CH2:12][CH:13]=[CH:14][CH2:15][CH2:16][CH2:17][C:18]([OH:20])=[O:19]>C(O)C>[OH:2][C@@H:3]([CH2:21][CH2:22][CH2:23][CH2:24][CH3:25])[CH:4]=[CH:5][CH:6]1[CH2:10][CH2:9][C:8](=[O:11])[CH:7]1[CH2:12][CH:13]=[CH:14][CH2:15][CH2:16][CH2:17][C:18]([OH:20])=[O:19]'
    s2 = 'A>>C'
    S1 = RecationSmile(s1)
    print(S1.getAgents())
    