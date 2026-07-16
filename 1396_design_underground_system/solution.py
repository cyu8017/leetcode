class UndergroundSystem:
    def __init__(self):self.ins={};self.stats={}
    def checkIn(self, id, stationName, t):self.ins[id]=(stationName,t)
    def checkOut(self, id, stationName, t):
        start,begin=self.ins.pop(id);total,count=self.stats.get((start,stationName),(0,0))
        self.stats[(start,stationName)]=(total+t-begin,count+1)
    def getAverageTime(self, startStation, endStation):
        total,count=self.stats[(startStation,endStation)];return total/count
