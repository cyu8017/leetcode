import heapq
class Solution:
    def maxEvents(self, events):
        events.sort(); h=[]; i=ans=day=0
        while i < len(events) or h:
            if not h: day=max(day, events[i][0])
            while i < len(events) and events[i][0] <= day:
                heapq.heappush(h, events[i][1]); i+=1
            while h and h[0] < day: heapq.heappop(h)
            if h: heapq.heappop(h); ans+=1; day+=1
        return ans
