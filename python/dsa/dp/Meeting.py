# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")

class Meeting:
    def __init__(self, name, hours):
        self.name = name
        self.hours = hours
        
    def __str__(self):
        return "Name: {}, Hours: {}".format(self.name, self.hours)
        
from typing import(List)
        
class MaxMeetings:
    def getMaxMeetings(self, meetings: List['Meeting'], haveHours: int) -> List['Meeting']:
        #sort meeting based on duration
        
        meetings.sort(key = lambda x: x.hours)
        
        #compile and return quickest meeting until haveHours is 0
        result = []
        
        print(meetings)
        for meeting in meetings:
            if meeting.hours <= haveHours:
                result.append(meeting)
                haveHours -= meeting.hours
                
        return result
        
        
        
meetings = [Meeting("One", 1), Meeting("Two", 5), Meeting("Three", 2), Meeting("Four", 3)]

meetingsUtil = MaxMeetings()
res = meetingsUtil.getMaxMeetings(meetings, 6)


for r in res:
    print(str(r))