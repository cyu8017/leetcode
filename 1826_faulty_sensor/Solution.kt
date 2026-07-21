// LeetCode 1826 - Faulty Sensor
// https://leetcode.com/problems/faulty-sensor/

class Solution {
    fun badSensor(sensor1: IntArray, sensor2: IntArray): Int {
        if (sensor1.contentEquals(sensor2)) return -1

        fun isDefective(correct: IntArray, faulty: IntArray): Boolean {
            val n = correct.size
            var i = 0
            while (i < n && correct[i] == faulty[i]) i++
            if (i == n) return false
            var j = i
            while (j < n - 1 && correct[j + 1] == faulty[j]) j++
            return j == n - 1
        }

        val sensor1Bad = isDefective(sensor2, sensor1)
        val sensor2Bad = isDefective(sensor1, sensor2)
        if (sensor1Bad && sensor2Bad) return -1
        if (sensor1Bad) return 1
        if (sensor2Bad) return 2
        return -1
    }
}
