
"""
import re

nombre1="Sandra Lóepez"

nombre2="Antonio Gómez"

nombre3="Sandra López"

if re.match("Sandra", nombre1, re.IGNORECASE):
    
    print("Hemos encontrado el nombre")
    
else:
    
    print("No lo hemos encontrado")
    """
    

import re

codigo1="jdshkfjhsdkfjhdskfjhsdkjh71hdgfjsdfhgsjdfhgsdjg"

codigo2="jfhdgsd71kjdhfkjsdhf ksjdhkfsdjh jh"

codigo3="ufdh_gdfhg_dh kdhg kjdfhgkjfd hkd"

if re.search("71", codigo1):
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado")