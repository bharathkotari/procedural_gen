# A small challenge to brush up your python skills
# here we are generating the world randomly 
# what you need to do ?
#1. create a player that accepts keyboard events(key press..etc)
#2. create some difficulties to the player
#3. use your creativity




import random
import time
import os
import numpy
rmax=20
cmax=20
r=rmax
c=cmax
f=numpy.zeros((r,c))
prev=random.randint(0,rmax-1)
height_limit=3
speed_delay=0.5

def fill_ground(i,j):
	for s in range(i+1,rmax):
		f[s,j]=2

def smoothing():
	for i in range(0,rmax):
		ra=random.randint(0,r-1)
		if ra==prev:
			f[ra,cmax-1]=1
			fill_ground(ra,cmax-1)
			break
		elif (ra>prev):
			f[ra+1,cmax-1]=1
			prev=ra
			fill_ground(ra,cmax-1)
			break
		else:
			f[ra-1,cmax-1]=1
			prev=ra
			fill_ground(prev,cmax-1)
			break


for j in range(0,c):

	for i in range(0,r):
		#print "prev="+str(prev) 
		ra=random.randint(0,r-1)
		#print ra,j,i
		if(i==ra) and (j>0)and (abs(prev-ra)<=height_limit):
			f[i,j]=1
			prev=ra
			#print"\t  in a"
			fill_ground(i,j)
			break
		elif (j==0) and (i==ra):
			f[i,j]=1
			prev=ra
			#print"\t in b"
			fill_ground(i,j)
			break
		elif (height_limit<abs(prev-ra)):
			ra=prev
			f[ra,j]=1
			#print"\tin c"
			fill_ground(i,j)
			break
		else:
			f[prev,j]=1
			#print"\t  in d"
			fill_ground(i,j)
			break
	prev=ra	
#print f
time.sleep(speed_delay)
os.system('clear')
#f=numpy.zeros((r,c))
while(1):
	
	for l in range(0,rmax):
		for k in range(0,cmax):
			if f[l,k]==1 :
				print "*",
			elif f[l,k]==2:
				print "!",
			else:
				print " ",
		print " "






	for m in range(0,cmax-1):
		for n in range(0,rmax):
			f[n,m]=f[n,m+1]
	for m in range (0,rmax):
		f[m,cmax-1]=0
	# smoothed noise generation here
 
	for i in range(0,rmax):
		ra=random.randint(0,r-1)
		if ra==prev:
			f[prev,cmax-1]=1
			fill_ground(prev,cmax-1)
			break
		elif (ra>prev):
			if(prev+1>=rmax-1):
				prev=prev-1
			if(f[prev,cmax-3]==1):
				f[prev+1,cmax-1]=1
				prev=prev+1
			elif ((f[prev,cmax-3]!=1)and(f[prev-1,cmax-3]==1)and (prev-1 >0)):
				f[prev+1,cmax-1]=1
				prev=prev+1	
			else:
				f[prev,cmax-1]=1
				prev=prev
			fill_ground(prev,cmax-1)
			break
		else:
			if (prev-1<=0):
				prev=prev+1
			if (f[prev,cmax-3]==1):
			
				f[prev-1,cmax-1]=1
				prev=prev-1
			elif ((f[prev,cmax-3]!=1)and(f[prev+1,cmax-3]==1)and (prev+1 <rmax)):
				f[prev-1,cmax-1]=1
				prev=prev-1	
			else:
				f[prev,cmax-1]=1
				prev=prev
			fill_ground(prev,cmax-1)
			break


	#sharp noise generated here
	'''for i in range(0,rmax):
		ra=random.randint(0,r-1)
		if ra==prev:
			f[ra,cmax-1]=1
			fill_ground(ra,cmax-1)
			break
		elif (ra!=prev) and (abs(ra-prev)<=height_limit):
			f[ra,cmax-1]=1
			prev=ra
			fill_ground(ra,cmax-1)
			break
		else:
			f[prev,cmax-1]=1
			fill_ground(prev,cmax-1)
			break'''
	time.sleep(speed_delay)
	os.system('clear')
	
	#print f


