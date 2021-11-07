from termcolor import *
import time
import random 
import math
def color(x,y):
	c = colored(x,y)
	print(c)
def ccc(x,y,z):
	colo = colored(x,y,z)
	print(colo)
ccc("                                         Made by Anish","red","on_green")
'''while True:
	passw = "A"
	pasi = input("first enter password\n>>>")
	if pasi==passw:
		print("Acess granted")
		break
	else:
		print("wrong password try again")'''
Na = input("my name is mark \U0001F600 \nwhat is your name ?\n>>>")
'''class mathfa(x):
	aaa = math.factorial(x)
	print(aaa)'''
fjfjjffj = colored("!instruction!\n if you enter invailed option then programe was end","green","on_red")
print(fjfjjffj)

print(f"oh nice name {Na}")
ccc("what you want to do \n1.math room\n2.timer\n3.mind reader game (no.1)\n4.rock paper scisser\n5.number guess game","green","on_red")
i = input(">>>")
def timer():
	sec=int(input("welcome to timer \nenter how many seconds you want to set in timet?\n>>>"))
	while sec>0:
		print(sec)
		sec=sec-1
		time.sleep(1)
	color("Time's up","red")
	ccc("                                                                                                            ","red","on_red")
def math():
	print("what you want to do ?\n1.percentage problems       2.to get factorial of any                                                number\n3.to get tables of any number  4.To covert second,days etc in real                                    time")
	mi = input(">>>")
	if mi=="1":
		print("choose a option \n1. convert any  percentage to number\n2.covert  any number  to percentage \n ")
		m2 = input(">>>")
		if m2=="1":
			print("example: Just i want how 3%  of 12 \n so first number is 12 and second was 3")
			m21 = int(input("enter first number \n>>>"))
			
			m22 = int(input("enter how many number you want percentage \n>>>"))
			ans =m21*m22/100
		print(ans)
		print(ans)
	if mi=="4":
		minp = input("1.second to days,hours,minutes,seconds\n enter number  >>> ")
		if minp=="1":
			mi_sec = int(input("enter seconds\n>>>"))
		a = mi_sec/60
		b = mi_sec%60
		c = mi_sec%60
		if a>60:
			a=a/60
			print(int(a),"hours")
		print(int(a),"minutes")
		if c!=0:
			print(c,"seconds")
		print("i am always right \U0001F600")
	if mi=="3":
			print("enter the number which you want table")
			num = int(input(">>>"))
			r = 1
			for i in range(1,11):
				nur = num*i
				#print(i)
				print(nur)
			print("\U0001F600your table was ready\U0001F600")
	if mi=="2":
			numd = input("enter number \n>>>")
			mathfa(numd)
			while r<=10:
				print(num*r)
				r=r+1
if i=="2":
	timer()
#rock paper scisser game
if i=="4":
	ccc("welcome to rock paper secicer game ","blue","on_green")
	rps = input("1.rock\n2.paper\n3.scisser\nenter your choice\n>>>")
	liast = ["rock","paper","scisser"]
	ran = random.choice(liast)
	ran = "rock"
	if rps=="1":
		rps="rock"
	if rps=="2":
		rps="paper"
	if rps=="3":
		rps="scisser"
	print(Na,"choice is",rps)
	print("mark choice is ",ran)
	if rps=="rock"and ran=="paper":
		winner = "mark"
		print("winner is",winner)
	if rps=="rock"and ran=="scisser":
		winner = Na
		print("winner is",winner)
	if rps=="paper"and ran=="scisser":
		winner = "mark"
		print("winner is",winner)
	if rps=="paper"and ran=="rock":
		winner = Na
		print("winner is",winner)
	if rps=="scisser"and ran=="paper":
		winner = Na
		print("winner is",winner)
	if rps=="scisser"and ran=="rock":
		winner = "mark"
		print("winner is",winner)
	if rps=="scisser"and ran=="scisser":
		winner ="match tie"
		print(winner)
	if rps=="paper"and ran=="paper":
			winner = "match tie"
			print(winner)
	if rps=="rock"and ran=="rock":
			winner = "match tie"
			print(winner)
#end				
if i=="1":
	math()
#number guess game
if i=="5":
	print("welcome to number guess game \nin this game mark think a number between 1 to 100 and you guess and enter the number if you guess corect number then you win")
	lll = int(input("1.easy(1 to 10)\n2.medium(1 to 50)\n3.hard(1 to 100)\n>>>"))
	level = 0
	if lll==1:
		lll=10
		print("number guessing range is 1 to 10(easy level)")
	elif lll==2:
		lll=50
		print("number guessing range is 50(medium level)")
	elif lll==3:
		lll=100
		print("number guessing range is 100(hard level)")
	else:
		colored("you not enter vailed option exit")
	guses = 15
	number = random.randrange(lll)
	while True:
		guses = guses-1
		inp = int(input("enter your guess number \n>>>"))
		if guses==0:
			print("you lose many wrong guses\n mark win the game")
			print(number)
			break
		if inp>number:
			ccc("so high try again","red","on_blue")
			print(f"you have {guses} more guses")
		if inp<number:
			ccc("so low try again","red","on_blue")
			print(f"you have {guses} more guses")
		if inp==number:
			print("\U0001F600you win the game")
			break
#mind reader game
def mrg():
	print("!instruction!\n1.think any two digit number \n2.add both\n3.subtract to your number\nexample:-  54 \n5+4=9\n54-9=45")
	input("you ready to play press enter:")
	input("Think two digit number \n<press enter>")
	input("Add both")
	input("subtract to your number ")
	print("see your number symbol:")
	l1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","@","#","&","%","$","?","¥","®"]
	ra = random.choice(l1)
	C = ["red","green","yellow"]
	K = random.choice(C)
	m = colored(ra,K)
	y1 = random.choice(l1)
	y2 = random.choice(l1)
	y3 = random.choice(l1)
	y4 = random.choice(l1)
	y5 = random.choice(l1)
	y6 = random.choice(l1)
	y7 = random.choice(l1)
	y8 = random.choice(l1)
	y9 = random.choice(l1)
	y10 = random.choice(l1)
	T1 = colored(y1,K)
	T2 = colored(y2,K)
	T3 = colored(y3,K)
	T4 = colored(y4,K)
	T5 = colored(y5,K)
	T6 = colored(y6,K)
	T7 = colored(y7,K)
	T8 = colored(y8,K)
	T9 = colored(y9,K)
	T10 = colored(y10,K)
	ra1 = colored(ra,"red")
	print("1.",T1,"    39.",T1,"    77.",T3)
	print("2.",T2, "  40.",T10,    "78.",T2)
	print("3.",T3,"    41.",T2,"    79.",T7)
	print("4.",T4,"    42.",T6,"    80.",T10)
	print("5.",T8,"    43.",T7,"    81.",m)
	print("6.",T4,"    44.",T2,"    82.",T4)
	print("7.",T10,"    45.",m,"    83.",T8)
	print("8.",T1,"    46.",T3,"    84.",T9)
	print("9.",m,"    47.",T1,"    85.",T1)
	print("10.",T8,"   48.",T8,
	"    85.",T6)
	print("11.",T7,"   49.",T9,"    86.",T5)
	print("12.",T3,"   50.",T10,"    87.",T2)
	print("13.",T5,"   51.",T4,"    88.",T8)
	print("14.",T1,"   52.",T6,"    89.",T4)
	print("15.",T9,"   53.",T7,"    90.",m)
	print("16.",T8,"   54.",m,"    91.",T5)
	print("17.",T2,"   55.",T1,"    92.",T7)
	print("18.",m,"   56.",T10,"    93.",T10)
	print("19.",T3,"   57.",T3,"    94.",T6)
	print("20.",T7,"   58.",T5,"    95.",T8)
	print("21.",T9,"   59.",T4,"    96.",T3)
	print("22.",T1,"   60.",T2,"    97.",T2)
	print("23.",T4,"   61.",T6,"    98.",T4)
	print("24.",T5,"   62.",T8,"    99.",m)
	print("25.",T2,"   63.",m,"   100.",T10)
	print("26.",T9,"   64.",T5,)
	print("27.",m,"   65.",T1)
	print("28.",T8,"   66.",T9)
	print("29.",T7,"   67."
	,T10)
	print("30.",T6,"   68.",T4)
	print("31.",T1,"   69.",T1)
	print("32.",T4,"   70.",T2)
	print("33.",T3,"   71.",T6)
	print("34.",T2,"   72.",m)
	print("35.",T5,"   73.",T7)
	print("36.",m,"   74.",T9)
	print("37.",T10,"   75.",T4)
	print("38.",T1,"   76.",T5)
	input("you see your symbol press enter:")
	print("reading minds....")
	time.sleep(2)
	print("your symbol was",ra1)
	s = input("IM right?\nY/N>>>")
	if s=="N":
	 z = int(input("enter first  number you think\n>>>"))
	 z1 = int(input("enter second number you think\n>>>"))
	 z2 = z+z1
	 print(f"{z}+{z1}={z2}")
	 zz1 = str(z)
	 zzz1 = str(z1)
	 z4 = zz1+zzz1
	 z5 = int(z4)-z2
	 print(z4,"-",z2,"=",z5)
	 print(z5,"=",ra)
	 print("Im sorry but your calculating was bad")
if i=="3":
	mrg()
#print("Good by see you later")
