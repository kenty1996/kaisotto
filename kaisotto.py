import sys, time, os

message = "Kai Sotto gustong i-posterized ang higante ng Jordan!\n\nhindi naman natakot si Scottie Thompson at nakipag agawan pa ng bola sa big man!\n\nsolid all-around performance mula sa MVP!!!\n\nito na mga bro Gilas Pilipinas laban sa home country ng Jordan.\n\nfirst time na nawala din sa line up ang Ravena brothers. First five ng pambandsang koponan--na'ndyan sila Kai Sotto, Japeth Aguilar, RR Pogoy, Dwight Ramos, at Scottie Thompson.\n\nwell, opening quarter, maaga tayong na 7 to 2 run ng kalaban. Primary defender ng itong Jordan si Dwight Ramos. Interesting rin ang tapatang Kai Sotto at Ahmad Al-Dwairi. Kung saan naisahan pa sa poste itong si Sotto. Though matapos ang run na 'yan, mabilis naman nakapick-up sa opensa ang Gilas mga bro! Kapansin-pansin 'yong napakagandang placing nila at 'yong solid ball movement led by Scottie Thompson! With already 3 assist sa first quarter!\n\n"
                        
for char in message:
	sys.stdout.write(char)
	sys.stdout.flush()
	time.sleep(0.1)

f = open("banner.txt", "r")
print(f.read())

