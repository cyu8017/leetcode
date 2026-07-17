# LeetCode 1826 - Faulty Sensor
# https://leetcode.com/problems/faulty-sensor/

from typing import List


class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        if sensor1 == sensor2:
            return -1

        def is_defective(correct: List[int], faulty: List[int]) -> bool:
            n = len(correct)
            i = 0
            while i < n and correct[i] == faulty[i]:
                i += 1
            if i == n:
                return False

            j = i
            while j < n - 1 and correct[j + 1] == faulty[j]:
                j += 1
            return j == n - 1

        sensor1_bad = is_defective(sensor2, sensor1)
        sensor2_bad = is_defective(sensor1, sensor2)

        if sensor1_bad and sensor2_bad:
            return -1
        if sensor1_bad:
            return 1
        if sensor2_bad:
            return 2
        return -1
