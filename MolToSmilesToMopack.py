from urllib.request import urlopen
from urllib.parse import quote

def CIRconvert(ids):
    try:
        url = 'http://cactus.nci.nih.gov/chemical/structure/' + quote(ids) + '/smiles' 
        ans = urlopen(url).read().decode('utf8')
        for line in ans:
            return ans
    except:
        return 'Did not work'
