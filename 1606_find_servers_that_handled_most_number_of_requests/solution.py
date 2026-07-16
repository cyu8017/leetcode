class Solution:
    def busiestServers(self, k, arrival, load):
        import heapq
        free = list(range(k)); busy = []; count = [0] * k
        for i, (t, length) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= t:
                _, server = heapq.heappop(busy)
                heapq.heappush(free, i + (server - i) % k)
            if not free: continue
            server = heapq.heappop(free) % k
            count[server] += 1; heapq.heappush(busy, (t + length, server))
        best = max(count)
        return [i for i, x in enumerate(count) if x == best]
