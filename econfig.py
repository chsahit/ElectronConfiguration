import sqlite3 as lite
from shells import *
con=None

def config(atomic_number):  
	configStr=''

	configStr=s1(atomic_number,configStr)
	atomic_number-=2

	configStr=s2(atomic_number,configStr)
	atomic_number-=2

	configStr=p2(atomic_number,configStr)	
	atomic_number-=6

	configStr=s3(atomic_number,configStr)
	atomic_number-=2

	configStr=p3(atomic_number,configStr)
	atomic_number-=6

	configStr=s4(atomic_number,configStr)
	atomic_number-=2

	configStr=d3(atomic_number,configStr)
	atomic_number-=10

	configStr=p4(atomic_number,configStr)
	atomic_number-=6

	configStr=s5(atomic_number,configStr)
        atomic_number-=2
	
	configStr=d4(atomic_number,configStr)
	atomic_number-=10

	configStr=p5(atomic_number,configStr)
	atomic_number-=6

	configStr=s6(atomic_number,configStr)
	atomic_number-=2

	configStr=f4(atomic_number,configStr)
	atomic_number-=14
	
	configStr=d5(atomic_number,configStr)
	atomic_number-=10

	configStr=p6(atomic_number,configStr)
	atomic_number-=6

	configStr=s7(atomic_number,configStr)
	atomic_number-=2

	configStr=f5(atomic_number,configStr)
	atomic_number-=14

	configStr=d6(atomic_number,configStr)
	atomic_number-=10
	
	configStr=p7(atomic_number,configStr)
	atomic_number-=6
	
	print "The electron configuration for this element is: "
        print configStr

if __name__=="__main__":
	print "Enter the symbol of an element on the periodic table"
	input=raw_input()
	try:
		con=lite.connect("~/documents/econf/pt")
		cur=con.cursor()
		cur.execute("SELECT atomicnumber FROM elements WHERE symbol='%s';"%input)
		data=cur.fetchone()
		con.close
		config(data[0])

	except lite.Error,e:
		print "error finding element"


			

