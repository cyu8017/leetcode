# LeetCode 0332 - Reconstruct Itinerary
# https://leetcode.com/problems/reconstruct-itinerary/

from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        targets: dict[str, list[str]] = defaultdict(list)
        for source, destination in sorted(tickets)[::-1]:
            targets[source].append(destination)

        route: list[str] = []

        def visit(airport: str) -> None:
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)

        visit("JFK")
        return route[::-1]
