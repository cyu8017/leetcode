from collections import deque
class FrontMiddleBackQueue:
    def __init__(self):
        self.l=deque();self.r=deque()
    def _bal(self):
        while len(self.l)>len(self.r)+1:self.r.appendleft(self.l.pop())
        while len(self.r)>len(self.l):self.l.append(self.r.popleft())
    def pushFront(self,val):self.l.appendleft(val);self._bal()
    def pushMiddle(self,val):
        if len(self.l)>len(self.r):self.r.appendleft(self.l.pop())
        self.l.append(val)
    def pushBack(self,val):self.r.append(val);self._bal()
    def popFront(self):
        if not self.l:return -1
        v=self.l.popleft();self._bal();return v
    def popMiddle(self):
        if not self.l:return -1
        v=self.l.pop();self._bal();return v
    def popBack(self):
        if not self.l:return -1
        v=self.r.pop() if self.r else self.l.pop();self._bal();return v
