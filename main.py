# ======================================================================
# PROJECT   : AUTO LOGIN 2.0
# AUTHOR    : RANJITH APPASSAMY
# DATE      : 18/02/2022
# ======================================================================

import dictionnaire as d

lien = ""
choixUser = 100

d.clear()

choixUser = d.AfficherMenuChoix()
d.clear

if(choixUser == 0) :
    exit()

elif (choixUser == 1) : 
    lien = d.dict_USMB["path_Intranet"]
    
elif (choixUser == 2) : 
    lien = d.dict_USMB["path_Moodle"]
    
elif (choixUser == 3) : 
    lien = d.dict_USMB["path_Scodoc"]
    


import fonction as f

f.openUSMB(lien)