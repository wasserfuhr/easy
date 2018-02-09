import subprocess
import os
for f in os.listdir("html"):
# fn=os.fsdecode(f)
 fn=f
 if fn.startswith("201"):
  c=subprocess.check_output("ls -l html/"+fn,shell=True).split(" ")
  h=format(int(c[4]),'x')
  print subprocess.check_output("sha256sum html/"+fn,shell=True).split(" ")[0]+" "+h
