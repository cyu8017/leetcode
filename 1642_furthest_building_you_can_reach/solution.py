class Solution:
    def furthestBuilding(self, heights, bricks, ladders):
        import heapq
        climbs=[]
        for i,d in enumerate(b-a for a,b in zip(heights,heights[1:])):
            if d<=0: continue
            heapq.heappush(climbs,d)
            if len(climbs)>ladders: bricks-=heapq.heappop(climbs)
            if bricks<0: return i
        return len(heights)-1
