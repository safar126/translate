import requests,os
from bs4 import BeautifulSoup
from time import sleep
logo = """#Author : Safar              #
#Support : My Team           #
#Team : From XiuzCode        #
#Tool : Translate            #
#My Contact : +6282288231535 #"""
def menu():
	os.system('clear') 
	print('='*30)
	print(logo)
	print("##########TRANSLATE###########")
	print("#1.Indonesia ke Inggris      #")
	print("#2.Inggris ke Indonesia      #")
	print('='*30)
	c = int(input("Pilih Translate : "))
	if c ==1:
		kontol1()
	elif c ==2:
		anjing()
	else:
		print("Masukkan Angka yang benar anjing... ")
		sleep(2)
		menu()
def kontol1():
	b = input("Bahasa indonesia : ")
	url = "https://mobile.sederet.com/translate.php"
	hed = {
	"User-Agent":"Mozilla/5.0 (Linux; Android 6.0.1; CPH1701) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36"
	}
	data = {"q":b, "lang":"id_en"}
	a = requests.post(url,data=data,headers=hed)
	soup = BeautifulSoup(a.text, "html.parser")#.json()
	#print(soup)
	for hasil in soup.find_all("div",class_="result_text"):
		print(hasil)
		#sleep(5)
		#menu()
def anjing():
	b = input("Bahasa Inggris : ")
	url = "https://mobile.sederet.com/translate.php"
	hed = {
	"User-Agent":"Mozilla/5.0 (Linux; Android 6.0.1; CPH1701) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36"
	}
	data = {"q":b, "lang":"en_id"}
	a = requests.post(url,data=data,headers=hed)
	soup = BeautifulSoup(a.text, "html.parser")#.json()
	#print(soup)
	for hasil in soup.find_all("div",class_="result_text"):
		print(hasil.text)
		#a = input("Apa mau lanjut? y/n : ")
		#if a =="y":
			#menu()
		#else:
			#print("Bye Bye Anjing... ")

menu()
