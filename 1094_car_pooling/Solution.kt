// LeetCode 1094 - Car Pooling
// https://leetcode.com/problems/car-pooling/

class Solution {
    fun carPooling(trips: Array<IntArray>, capacity: Int): Boolean {
        val diff = IntArray(1001)
        for (t in trips) {
            diff[t[1]] += t[0]
            diff[t[2]] -= t[0]
        }
        var cur = 0
        for (x in diff) {
            cur += x
            if (cur > capacity) return false
        }
        return true
    }
}
