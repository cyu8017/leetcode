# LeetCode 2877 - Create a DataFrame from List
# https://leetcode.com/problems/create-a-dataframe-from-list/

from typing import Any, List


class Solution:
    def createDataframe(self, student_data: List[List[int]]) -> List[Any]:
        return [{"student_id": student_id, "age": age} for student_id, age in student_data]
