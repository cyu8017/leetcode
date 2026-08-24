// LeetCode 3594 - Minimum Time to Transport All Individuals
// https://leetcode.com/problems/minimum-time-to-transport-all-individuals/

class Solution {
    fun minTime(n: Int, k: Int, m: Int, time: IntArray, mul: DoubleArray): Double {
        var t = time.clone()
        t.sort()
        var total = 0
        var stage = 0
        var left = n
        while (left > 0) {
            var take = minOf(k, left)
            var slow = t[left - 1]
            total += slow * mul[stage % m]
            left -= take
            stage = stage + 1
            if (left > 0) {
                total += t[0] * mul[stage % m]
                stage = stage + 1
            }
        }
        return total
    }
}
