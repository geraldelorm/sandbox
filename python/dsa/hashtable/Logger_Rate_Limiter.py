class LogLimiter:
    def __init__(self):
        self.messagetimestamps = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.messagetimestamps:
            self.messagetimestamps[message]  = timestamp
            return True
        
        exsiting_timestamp = self.messagetimestamps[message]
        self.messagetimestamps[message] = timestamp

        return timestamp - exsiting_timestamp >= 10

# TC: O(1)
# SC: O(n)

#Test -----

myLogger = LogLimiter()

assert(myLogger.shouldPrintMessage(1, "foo") == True)
assert(myLogger.shouldPrintMessage(4, "foo") == False)
assert(myLogger.shouldPrintMessage(14, "foo") == True)
print("All tests passed!")