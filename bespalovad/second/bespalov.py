#Програма обчислює день тижня за датою

import re

def readDate ():
	date = input ("Введіть дату у форматі DD-MM-YYYY: ")
	while not bool (re.match(r'(( (([0][1..9]) | ([1][0..9]) | ([2][0..8])) [-] (([0][1..9]) | ([1][0..2])) [-]\d\d\d\d) | ([2][9][-][0][2][-]\d\d (([02468][48]) | ([13579][260])) ) | ([3][0][-] ([0][13456789] | [1][0..2]) \d\d\d[1..9]) | ([3][1][-] (([0][13578]) | ([1][02])) \d\d\d\d))\Z', date)):
		date = input ("Дата не існує. Введіть іншу: ")
	date_list = date.split("-")
	return (date_list)

def weekDay (date_list):
	delta = int(date_list[0])
	if date_list[1] == "01":
		delta +=4
	if date_list[1] == "02":
		delta +=5
	if date_list[1] == "03":
		delta +=9
	if date_list[1] == "04":
		delta +=12
	if date_list[1] == "05":
		delta +=16
	if date_list[1] == "06":
		delta +=19
	if date_list[1] == "07":
		delta +=23
	if date_list[1] == "08":
		delta +=27
	if date_list[1] == "09":
		delta +=30
	if date_list[1] == "10":
		delta +=34
	if date_list[1] == "11":
		delta +=37
	if date_list[1] == "12":
		delta +=41
	delta += 5*int( int(date_list[2])/4 )
	delta += int(date_list[2]) mod 4
	delta = delta mod 7
	if delta == 0:
		return ("Понеділок")
	if delta == 1:
		return ("Вівторок")
	if delta == 2:
		return ("Середа")
	if delta == 3:
		return ("Четвер")
	if delta == 4:
		return ("П'ятниця")
	if delta == 5:
		return ("Субота")
	if delta == 6:
		return ("Неділя")

def main ():
	print (weekDay(readDate()))

main ()
