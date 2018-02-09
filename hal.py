import os
for f in os.listdir("."):
 print os.system("ls -l "+f).split(" ")[2]
