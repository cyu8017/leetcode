import heapq

class Solution:
    def longestDiverseString(self, a, b, c):
        heap = [(-count, char) for count, char in ((a, "a"), (b, "b"), (c, "c")) if count]
        heapq.heapify(heap)
        answer = []
        while heap:
            count, char = heapq.heappop(heap)
            if len(answer) >= 2 and answer[-1] == answer[-2] == char:
                if not heap:
                    break
                count2, char2 = heapq.heappop(heap)
                answer.append(char2)
                if count2 + 1:
                    heapq.heappush(heap, (count2 + 1, char2))
                heapq.heappush(heap, (count, char))
            else:
                answer.append(char)
                if count + 1:
                    heapq.heappush(heap, (count + 1, char))
        return "".join(answer)
