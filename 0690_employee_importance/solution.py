# LeetCode 0690 - Employee Importance
# https://leetcode.com/problems/employee-importance/

from typing import List, Union


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(
        self, employees: List[Union[Employee, list]], id: int
    ) -> int:
        table: dict[int, tuple[int, list[int]]] = {}
        for emp in employees:
            if isinstance(emp, list):
                eid, importance, subordinates = emp
            else:
                eid, importance, subordinates = emp.id, emp.importance, emp.subordinates
            table[eid] = (importance, subordinates)

        def dfs(eid: int) -> int:
            importance, subordinates = table[eid]
            return importance + sum(dfs(sub) for sub in subordinates)

        return dfs(id)
