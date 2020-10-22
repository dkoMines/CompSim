from numpy import random
import sys

class Event():
    def __init__(self, at, eventType, service):
        self.at = at
        self.eventType = eventType
        self.service = service

if __name__ == '__main__':
    numServers = int(sys.argv[1])
    servers = 0
    eventList = []
    t = 0
    T = 1000
    jobQueue = []
    inService = False
    numBusy = 0

    #statistics
    newJobCount = 0
    jobsServiced = 0

    v = []

    ev1 = Event(random.exponential(2.0), 'ArrivalEvent', random.uniform(0.0, 2.0))
    eventList.append(ev1)

    while(len(eventList)>0):
    #while(t<=T & len(eventList)>0):
        eventList.sort(key=lambda x: x.at)
        eventInQ = eventList[0]
        eventList.pop(0)
        t = eventInQ.at
        # Event Arrived or feedback event
        if(eventInQ.eventType=='ArrivalEvent' or eventInQ.eventType=='FeedbackEvent'):
            if(eventInQ.eventType=='ArrivalEvent'):
                newJobCount+=1
                newArrTime = (random.exponential(2.0)+t)
                if(newArrTime<T):
                    newArrival = Event(newArrTime, 'ArrivalEvent', random.uniform(0.0, 2.0))
                    eventList.append(newArrival)
            jobQueue.append(eventInQ)
        # Job Complete
        elif(eventInQ.eventType=='JobCompleteEvent'):
            feedbackChance = random.uniform(0.0,1.0)
            if(feedbackChance<0.25):
                feedbackEvent = Event((t+random.exponential(1.0)), 'FeedbackEvent', (eventInQ.service/2.0))
                eventList.append(feedbackEvent)
            servers -= 1
        if(servers < numServers and len(jobQueue)>0):
            eventInQ = jobQueue[0]
            jobQueue.pop(0)
            eventInQ.at = (eventInQ.service+t)
            eventInQ.eventType = 'JobCompleteEvent'
            eventList.append(eventInQ)
            servers += 1
            jobsServiced+=1
        rN = random.exponential(2.0)
        if rN > 1.6:
            v.append(servers)
    print("t value: "+str(t)+" New Job Count: "+str(newJobCount)+" Jobs Serviced: "+str(jobsServiced))
    lv = 0
    bv = len(v)
    avg = sum(v)/bv
    sd = 0
    for num in v:
        if num > numServers/2:
            lv += 1
            sd += (num-avg)**2
    sd = (sd/bv)**.5
    print(f'Avg = {avg} sd = {sd}')
    print(f'%={lv/bv} v={lv} big_V={bv}')
