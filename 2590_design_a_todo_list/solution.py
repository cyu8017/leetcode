# LeetCode 2590 - Design a Todo List
# https://leetcode.com/problems/design-a-todo-list/

from typing import List


class TodoList:
    def __init__(self):
        self.nextID = 1
        self.tasks = {}
        self.users = {}

    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: List[str]) -> int:
        tid = self.nextID
        self.nextID += 1
        self.tasks[tid] = {
            "id": tid,
            "description": taskDescription,
            "dueDate": dueDate,
            "userId": userId,
            "tags": set(tags),
            "done": False,
        }
        if userId not in self.users:
            self.users[userId] = []
        self.users[userId].append(tid)
        return tid

    def getAllTasks(self, userId: int) -> List[str]:
        if userId not in self.users:
            return []
        ids = self.users[userId][:]
        ids.sort(key=lambda i: self.tasks[i]["dueDate"])
        ans = []
        for tid in ids:
            if not self.tasks[tid]["done"]:
                ans.append(self.tasks[tid]["description"])
        return ans

    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
        if userId not in self.users:
            return []
        ids = self.users[userId][:]
        ids.sort(key=lambda i: self.tasks[i]["dueDate"])
        ans = []
        for tid in ids:
            tk = self.tasks[tid]
            if not tk["done"] and tag in tk["tags"]:
                ans.append(tk["description"])
        return ans

    def completeTask(self, userId: int, taskId: int) -> None:
        tk = self.tasks.get(taskId)
        if not tk or tk["userId"] != userId or tk["done"]:
            return
        tk["done"] = True
