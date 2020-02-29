# fname = 'regex_sum_42.txt' # SAMPLE
fname = 'regex_sum_367892.txt' # ACTUAL

import re
print( sum( [ int(i) for i in re.findall(r'\d+',open(fname).read()) ] ) )