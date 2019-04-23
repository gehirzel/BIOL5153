#! /usr/bin/env python3
import re
text ="Katherine went to the concert to see her favorite band, Catheryn and the Cathryn’s. She ran into her friend Kathryn, who introduced Katherine to her friend, Catherine. Together, they enjoyed the concert while texting inaudible snippets to their mutual friends, Kathrin and katharine." 
#more elegant way to use vertical bar for K & C??
match = re.findall(r"(Kath.?r.?n.?|Cath.?r.?n.?)", text, flags=re.IGNORECASE)
print (match)
