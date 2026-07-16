class Solution:
    def busyStudent(self, startTime, endTime, queryTime):
        return sum(start <= queryTime <= end for start, end in zip(startTime, endTime))
