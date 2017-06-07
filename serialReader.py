import time
import serial
from pymongo import MongoClient

#
# ser = serial.Serial('/dev/cu.usbmodem1431',9600)
# ser.timeout = 7
client = MongoClient("mongodb://localhost:27017")

db = client['plants']
plants= db.plants
#
# def sendHumidityRequest():
#     send= "humidity"
#     ser.write(send)
#
# def sendWaterRequest():
#     send = "water"
#     ser.write(send)
#
#
# def readResponse():
#     return ser.readline()

def get_last_humidity_data():
    pipeline = [{"$match":
                     {"plant_id": 1}
                 },
                {"$unwind": "$humidity_data"},
                {"$sort":
                     {"humidity_data.date": -1}
                 },
                {"$limit": 1},
                {"$project":
                     {"_id": 0, "humidity_data.humidity": 1}
                 }
                ]
    return list(db.plants.aggregate(pipeline))

def get_humidity_threshold():
    pipeline = [{ "$match":
                      { "plant_id": 1 }
                  },
                { "$unwind": "$humidity_constants"},
                { "$sort":
                      { "humidity_constants.date": -1}
                  },
                {"$limit": 1},
                {"$project":
                    {"_id": 0, "humidity_constants.threshold": 1}
                 }
                ]
    return list(db.plants.aggregate(pipeline))


print get_last_humidity_data()
print get_humidity_threshold()



# while True:
#     #sendHumidityRequest()
#     time.sleep(2)
#     #response=readResponse()
#     response = ["h", 3]
#     print(response)
#     if (len(response) > 0 and response[0] == "h"):
#         h_value = response[1:]
#         timestamp = int(time.time())
#         assert isinstance(plants, object)
#         plants.update({plant_id: 1}, {"$push": {"humidity_data": {"date" : time.time(),"humidity": h_value}}})
#         if h_value > 10:
#             sendWaterRequest()
#             print(readResponse())
#     time.sleep(10)