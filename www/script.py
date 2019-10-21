import sys
request = sys.stdin.readline()
print("<br><h3>request: </h3>",)
print(request,end="<br>")
print("<br>", type(request),"<br>")
print("<br>","<h3>globals():</h3> ", globals(),"<br>")
print("""
<br><input/><button>OK</button>
""")
print("<h3>for a in range(1,100):</h3> ")
for a in range(1,100):
    print('<h1>',a,'</h1>',end='')