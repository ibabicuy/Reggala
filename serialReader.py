import time
import serial


ser = serial.Serial('/dev/cu.usbmodem1431',9600)
ser.timeout = 7;


def sendHumidityRequest():
	send= "humidity"
	ser.write(send)

def sendWaterRequest():
	send = "water"
	ser.write(send)


def readResponse():
	return ser.readline()



while True:
	sendHumidityRequest();
	time.sleep(2)
	response=readResponse();
	print(response)
	if len(response) > 0 and response[0] == "h" :
		h_value = response[1:]
		if h_value > 10:
			sendWaterRequest();
			print(readResponse())


