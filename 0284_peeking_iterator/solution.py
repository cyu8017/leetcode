# LeetCode 0284 - Peeking Iterator
# https://leetcode.com/problems/peeking-iterator/


class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self._peeked = None
        self._has_peeked = False

    def peek(self) -> int:
        if not self._has_peeked:
            self._peeked = self.iterator.next()
            self._has_peeked = True
        return self._peeked

    def next(self) -> int:
        if self._has_peeked:
            result = self._peeked
            self._peeked = None
            self._has_peeked = False
            return result
        return self.iterator.next()

    def hasNext(self) -> bool:
        return self._has_peeked or self.iterator.hasNext()
