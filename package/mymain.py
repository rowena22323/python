"""
import mymod2
mymod2.myfunc() # module file이 다른곳으로 옮겨가면 읽을 수 없다!

import sys
print(sys.path) # PYTHONPATH
sys.path.append("C:\\Python_modules2")

import mymod2
mymod2.myfunc()
"""
from package.func1 import function5

function5()
