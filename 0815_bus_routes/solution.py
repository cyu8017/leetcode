# LeetCode 0815 - Bus Routes
# https://leetcode.com/problems/bus-routes/

from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0
        stop_to_buses: dict[int, list[int]] = defaultdict(list)
        for bus, stops in enumerate(routes):
            for stop in stops:
                stop_to_buses[stop].append(bus)

        queue = deque([(source, 0)])
        seen_stops = {source}
        seen_buses: set[int] = set()
        while queue:
            stop, buses_taken = queue.popleft()
            for bus in stop_to_buses[stop]:
                if bus in seen_buses:
                    continue
                seen_buses.add(bus)
                for nxt in routes[bus]:
                    if nxt == target:
                        return buses_taken + 1
                    if nxt not in seen_stops:
                        seen_stops.add(nxt)
                        queue.append((nxt, buses_taken + 1))
        return -1
