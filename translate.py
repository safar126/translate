import requests,os
from time import sleep
import time; 
localtime = time.asctime(time.localtime(time.time()))
#print "Waktu lokal saat ini :", localtime
r = '\033[1;31m'
h = '\033[1;32m'
k = '\033[1;33m'
p = '\033[1;0m'
def logo():
	print(r+"___ ____ ____ _  _ ____ _    ____ ___ ____ ")
	print(k+" |  |__/ |__| |\ | [__  |    |__|  |  |___ ")
	print(h+" |  |  \ |  | | \| ___] |___ |  |  |  |___ ")

def menu():
	os.system('clear') 
	logo()
	print (p+" Waktu lokal saat ini :\n\b",localtime)
	print(h+" Author : Safar")
	print(" Team : XiuzCode")
	print(h+" 1.Translate All Bahasa    ")
	print(" 2.Dapatkan Code Negara     ")
	print(r+'='*30)
	c = input(p+" Pilih No : ")
	try:
		if c =="1":
			kontol1()
		elif c =="2":
			daftar()
		else:
			print(k+" Masukkan Angka yang benar anjing... ")
			sleep(2)
			menu()
	except ValueError:
		pass



def kontol1():
	print(" Note : Program ini di butuhkan Kode Negara\n Jika kalian belum punya kode nya\n Silahkan ambil kodenya di menu kedua\n Contoh : \n Kode pertama : id\n Kode kedua : en")
	kode = input(h+" Masukkan Kode Negara pertama : ")
	kode2 = input(h+" Masukkan Kode Negara Kedua : ")
	aa = input(" Masukan Text : ")
	ss = requests.get(r"https://translate.google.com/translate_a/t?client=at&sc=1&v=2.0&sl="+kode+"&tl="+kode2+"&hl=nl&ie=UTF-8&oe=UTF-8&text="+aa).json()
	for x in ss["sentences"]:
		print(r+'='*30)
		print(h+" Bahasa "+kode+" : ",aa) 
		print (" Bahasa "+kode2+" : ",x["trans"])
		print(r+"="*30)
		x = input(k+" Tekan Enter Buat Kembali kemenu ")
		if x =="":
			menu()


def daftar():
	print(k+"""
	[{ Code Negara  Nama Negara}],
	{code:'af',name:'Afrikans'},
	{code:'sq',name:'Albania'},
	{code:'am',name:'Amhara'},
	{code:'ar',name:'Arab'},
	{code:'hy',name:'Armenia'},
	{code:'az',name:'Azerbaijan'},
	{code:'eu',name:'Basque'},
	{code:'nl',name:'Belanda'},
	{code:'be',name:'Belarussia'},
	{code:'bn',name:'Bengali'},
	{code:'bs',name:'Bosnia'},
	{code:'bg',name:'Bulgaria'},
	{code:'my',name:'Burma'},
	{code:'ceb',name:'Cebuano'},
	{code:'cs',name:'Ceko'},
	{code:'ny',name:'Chichewa'},
	{code:'zh-CN',name:'China'},
	{code:'da',name:'Denmark'},
	{code:'eo',name:'Esperanto'},
	{code:'et',name:'Estonia'},
	{code:'fa',name:'Farsi'},
	{code:'fi',name:'Finlandia'},
	{code:'fy',name:'Frisia'},
	{code:'ga',name:'Gaelig'},
	{code:'gd',name:'Gaelik Skotlandia'},
	{code:'gl',name:'Galisia'},
	{code:'ka',name:'Georgia'},
	{code:'gu',name:'Gujarati'},
	{code:'ha',name:'Hausa'},
	{code:'haw',name:'Hawaii'},
	{code:'hi',name:'Hindi'},
	{code:'hmn',name:'Hmong'},
	{code:'iw',name:'Ibrani'},
	{code:'ig',name:'Igbo'},
	{code:'id',name:'Indonesia'},
	{code:'en',name:'Inggris'},
	{code:'is',name:'Islan'},
	{code:'it',name:'Italia'},
	{code:'jw',name:'Jawa'},
	{code:'ja',name:'Jepang'},
	{code:'de',name:'Jerman'},
	{code:'kn',name:'Kannada'},
	{code:'ca',name:'Katala'},
	{code:'kk',name:'Kazak'},
	{code:'km',name:'Khmer'},
	{code:'rw',name:'Kinyarwanda'},
	{code:'ky',name:'Kirghiz'},
	{code:'ko',name:'Korea'},
	{code:'co',name:'Korsika'},
	{code:'ht',name:'Kreol Haiti'},
	{code:'hr',name:'Kroat'},
	{code:'ku',name:'Kurdi'},
	{code:'lo',name:'Laos'},
	{code:'la',name:'Latin'},
	{code:'lv',name:'Latvia'},
	{code:'lt',name:'Lituania'},
	{code:'lb',name:'Luksemburg'},
	{code:'hu',name:'Magyar'},
	{code:'mk',name:'Makedonia'},
	{code:'mg',name:'Malagasi'},
	{code:'ml',name:'Malayalam'},
	{code:'mt',name:'Malta'},
	{code:'mi',name:'Maori'},
	{code:'mr',name:'Marathi'},
	{code:'ms',name:'Melayu'},
	{code:'mn',name:'Mongol'},
	{code:'ne',name:'Nepal'},
	{code:'no',name:'Norsk'},
	{code:'or',name:'Odia (Oriya)'},
	{code:'ps',name:'Pashto'},
	{code:'pl',name:'Polandia'},
	{code:'pt',name:'Portugis'},
	{code:'fr',name:'Prancis'},
	{code:'pa',name:'Punjabi'},
	{code:'ro',name:'Rumania'},
	{code:'ru',name:'Rusia'},
	{code:'sm',name:'Samoa'},
	{code:'sr',name:'Serb'},
	{code:'st',name:'Sesotho'},
	{code:'sn',name:'Shona'},
	{code:'sd',name:'Sindhi'},
	{code:'si',name:'Sinhala'},
	{code:'sk',name:'Slovakia'},
	{code:'sl',name:'Slovenia'},
	{code:'so',name:'Somali'},
	{code:'es',name:'Spanyol'},
	{code:'su',name:'Sunda'},
	{code:'sw',name:'Swahili'},
	{code:'sv',name:'Swensk'},
	{code:'tl',name:'Tagalog'},
	{code:'tg',name:'Tajik'},
	{code:'ta',name:'Tamil'},
	{code:'tt',name:'Tatar'},
	{code:'te',name:'Telugu'},
	{code:'th',name:'Thai'},
	{code:'tr',name:'Turki'},
	{code:'tk',name:'Turkmen'},
	{code:'uk',name:'Ukraina'},
	{code:'ur',name:'Urdu'},
	{code:'ug',name:'Uyghur'},
	{code:'uz',name:'Uzbek'},
	{code:'vi',name:'Vietnam'},
	{code:'cy',name:'Wales'},
	{code:'xh',name:'Xhosa'},
	{code:'yi',name:'Yiddi'},
	{code:'yo',name:'Yoruba'},
	{code:'el',name:'Yunani'},
	{code:'zu',name:'Zulu'}""")
	lonte = input(r+"\nTEKAN ENTER UNTUK KEMBALI... ")
	menu()

	
	
	
menu()
