# LeetCode 3408 - Design Task Manager
# https://leetcode.com/problems/design-task-manager/

from typing import List


class TaskManager:
    def __init__(self, tasks: List[List[int]]) -> None:
        self.pri = {}
        self.user = {}
        self.h = []
        for t in tasks:
            self.add(t[0], t[1], t[2])

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.pri[taskId] = priority
        self.user[taskId] = userId
        self.h.append([priority, taskId, userId])

    def edit(self, taskId: int, newPriority: int) -> None:
        self.pri[taskId] = newPriority
        self.h.append([newPriority, taskId, self.user[taskId]])

    def rmv(self, taskId: int) -> None:
        self.pri.pop(taskId, None)
        self.user.pop(taskId, None)

    def execTop(self) -> int:
        self.h.sort(key=lambda a: (a[0], a[1]))
        while self.h:
            top = self.h.pop()
            p = self.pri.get(top[1])
            if p is not None and p == top[0] and self.user.get(top[1]) == top[2]:
                del self.pri[top[1]]
                uid = self.user.get(top[1])
                del self.user[top[1]]
                return uid
        return -1
