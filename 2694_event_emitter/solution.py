# LeetCode 2694 - Event Emitter
# https://leetcode.com/problems/event-emitter/

from typing import Any, Callable, Dict, List


class EventEmitter:
    def __init__(self):
        self.handlers: Dict[str, List[Callable]] = {}

    def subscribe(self, eventName: str, callback: Callable) -> Dict[str, Callable]:
        if eventName not in self.handlers:
            self.handlers[eventName] = []
        lst = self.handlers[eventName]
        lst.append(callback)

        def unsubscribe() -> None:
            if callback in lst:
                lst.remove(callback)

        return {"unsubscribe": unsubscribe}

    def emit(self, eventName: str, args: List[Any] = None) -> List[Any]:
        if args is None:
            args = []
        lst = self.handlers.get(eventName, [])
        return [cb(*args) for cb in lst]


class Solution:
    def EventEmitter(self, actions: Any = None, values: Any = None) -> EventEmitter:
        return EventEmitter()
