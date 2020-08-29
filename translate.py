import requests,os
from time import sleep
import time; 
localtime = time.asctime(time.localtime(time.time()))
#print "Waktu lokal saat ini :", localtime

logo = """#Author : Safar              #
#Support : My Team           #
#Team : From XiuzCode        #
#Tool : Translate            #
#My Contact : +6282288231535 #"""
def menu():
	os.system('clear') 
	print ("Waktu lokal saat ini :\n\b",localtime)
	print('='*30)
	print(logo)
	print("##########TRANSLATE###########")
	print("#1.Indonesia ke Inggris      #")
	print("#2.Inggris ke Indonesia      #")
	print('='*30)
	c = input("Pilih Translate : ")
	try:
		if c =="1":
			kontol1()
		elif c =="2":
			anjing()
		else:
			print("Masukkan Angka yang benar anjing... ")
			sleep(2)
			menu()
	except ValueError:
		pass
def anjing():
	aa = input("Translate : ")
	ss = requests.get(r"https://translate.google.com/translate_a/t?client=at&sc=1&v=2.0&sl=en&tl=id&hl=nl&ie=UTF-8&oe=UTF-8&text="+aa).json()
	for x in ss["sentences"]:
		print('='*30)
		print("Bahasa inggris : ",aa) 
		print ("Bahasa indonesia ",x["trans"])
		print("="*30)
		print("Tekan Enter Buat Kembali kemenu")
		x = input()
		if x =="":
			menu()

def kontol1():
	aa = input("Translate : ")
	ss = requests.get(r"https://translate.google.com/translate_a/t?client=at&sc=1&v=2.0&sl=id&tl=en&hl=nl&ie=UTF-8&oe=UTF-8&text="+aa).json()
	for x in ss["sentences"]:
		print('='*30)
		print("Bahasa indonesia : ",aa) 
		print ("Bahasa inggris : ",x["trans"])
		print("="*30)
		print("Tekan Enter Buat Kembali kemenu")
		x = input()
		if x =="":
			menu()
menu()


