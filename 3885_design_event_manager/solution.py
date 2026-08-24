# LeetCode 3885 - Design Event Manager
# https://leetcode.com/problems/design-event-manager/

from typing import Dict, List


class EventManager:
    def __init__(self, events: List[List[int]]):
        self.sl: List[List[int]] = []
        self.d: Dict[int, int] = {}
        for e in events:
            event_id, priority = e[0], e[1]
            self.sl.append([-priority, event_id])
            self.d[event_id] = priority
        self._sort()

    def _sort(self) -> None:
        self.sl.sort(key=lambda a: (a[0], a[1]))

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        old = self.d[eventId]
        self.sl = [x for x in self.sl if not (x[0] == -old and x[1] == eventId)]
        self.sl.append([-newPriority, eventId])
        self.d[eventId] = newPriority
        self._sort()

    def pollHighest(self) -> int:
        if not self.sl:
            return -1
        top = self.sl.pop(0)
        event_id = top[1]
        del self.d[event_id]
        return event_id
