#! /usr/bin/env python3

import re

katherine = "Katherine went to the concert to see her favorite band, Catheryn and the Cathryn’s. She ran into her friend Kathryn, who introduced Katherine to her friend, Catherine. Together, they enjoyed the concert while texting inaudible snippets to their mutual friends, Kathrin and katharine";
match = re.findall(".ath[a-z]*", katherine)
if match:
  print(match) 
else:
  print('did not find')