from time import sleep
from datetime import datetime
from json import load,dump
from os import system
import random
import string
upper_case = string.ascii_uppercase

def menu():
	print("1.Show ticket")
	print("2.Order ticket")
	print("3.Cancel ticket")
	print("Q.Quit")

def print_ticket(data):
	system("cls")
	num = 1
	for id_data in data:
		code = data[id_data]["booking_code"]
		pes = data[id_data]["pessenger"]
		org = data[id_data]["origin"]
		dst = data[id_data]["destination"]
		time = data[id_data]["time"]
		terminal = data[id_data]["terminal"]
		airline = data[id_data]["airline"]
		seat = data[id_data]["seat"]
		kles = data[id_data]["class"]
		baggage = data[id_data]["baggage"]
		print(f"{num}. ID: {id_data} -- Booking Code: {code} -- pessenger data: {pes} -- origin data: {org} -- destination data: {dst} -- time data: {time} -- terminal: {terminal} -- airline: {airline} -- seat: {seat} -- class: {kles} -- baggage: {baggage}")
		num += 1
	input("Press enter to back")

def booking_code_generator():
	return (f"{random.choice(upper_case)}{random.choice(upper_case)}{random.choice(upper_case)}{random.randint(1,99)}")

def pessenger_info():
	info = []
	title = string.capwords(input("Input your title: "))
	front = string.capwords(input("Input your front name: "))
	last = string.capwords(input("Input your last name: "))
	info.append(title)
	info.append(front)
	info.append(last)
	return info

def origin_info():
	info = []
	city = string.capwords(input("Input your origin city: "))
	airport = input("Input your origin airport: ").upper()
	info.append(city)
	info.append(airport)
	return info

def destination_info():
	info = []
	city = string.capwords(input("Input your destination city: "))
	airport = input("Input your destination airport: ").upper()
	info.append(city)
	info.append(airport)
	return info

def time_info():
	info = []
	check_in = input("Input check in time: ")
	boarding = input("Input boarding time: ")
	arrival = input("Input arrival time: ")
	info.append(check_in)
	info.append(boarding)
	info.append(arrival)
	return info

def verify(ans):
	if ans.upper()=="Y":
		return True
	else:
		return False

def create_id_data(plane):
	day_now = datetime.now()
	yr = day_now.year
	mnt = day_now.month
	day = day_now.day
	id_data = ("%04d%02d%02d-%s%i"%(yr,mnt,day,plane[0],random.randint(0,9999)))
	return id_data

def order_ticket():
	system("cls")
	booking_code = booking_code_generator()
	pessenger = pessenger_info()
	origin = origin_info()
	destination = destination_info()
	time = time_info()
	terminal = (f"{random.randint(1,9)}{random.choice(upper_case)}")
	airlines = string.capwords(input("Input your airlines: "))
	seat = (f"{random.randint(1,50)}{random.choice(upper_case)}")
	klas = input("Choose your class (business or economy): ")
	bag = float(input("Input your extra baggage: "))
	respon = input("are you sure you want to book a ticket (Y/N)? ")
	if verify(respon):
		id_data = create_id_data(airlines)
		ticket_data[id_data]={
		"booking_code" : booking_code,
		"pessenger" : {
			"title" : pessenger[0],
			"front_name" : pessenger[1],
			"last_name" : pessenger[2]
			},
		"origin" : {
			"city" : origin[0],
			"airport" : origin[1]
			},
		"destination" : {
			"city" : destination[0],
			"airport" : destination[1]
			},
		"time" : {
			"check_in" : time[0],
			"boarding" : time[1],
			"arrival" : time[2]
			},
		"terminal" : terminal,
		"airline" : airlines,
		"seat" : seat,
		"class" : klas,
		"baggage" : bag
		}
		saved = save_ticket()
		if saved:
			print("Data has been saved")
		else:
			print("Failed to saved data")
	else:
		print("aborting the order")
		print("please wait")
		sleep(3)
	input("Press enter to back")

def cancel_ticket():
	system("cls")
	search_id = input("Input your flight code (ex. 20200611-G0001): ")
	for id_data in ticket_data:
		if id_data == search_id:
			respon = input("Are you sure to cancel the ticket order? ")
			verify(respon)
			if verify:
				del ticket_data[search_id]
				saved = save_ticket()
				if saved:
					print("Ticket has been canceled")
				else:
					print("Failed to cancel ticket")
			else:
				print("Aborting")
	input("Press enter to back")

def user_input_check(ans):
	system("cls")
	ans = ans.upper()
	if ans == "Q":
		return True
	elif ans == "1":
		print_ticket(ticket_data)
	elif ans == "2":
		order_ticket()
	elif ans == "3":
		cancel_ticket()

def load_ticket():
	with open(ticket_path, "r")as ticketFile:
		data = load(ticketFile)
	return data

def save_ticket():
	with open(ticket_path, "w")as ticketFile:
		dump(ticket_data, ticketFile)
	return True

stop = False
ticket_path = "Data_ticket/data_ticket.json"
ticket_data = load_ticket()

while not stop:
	system("cls")
	menu()
	user_choice = input("Input your choice: ")
	stop = user_input_check(user_choice)