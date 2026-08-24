// LeetCode 3301 - Maximize the Total Height of Unique Towers
// https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/

class Solution {
    fun maximumTotalSum(maximumHeight: IntArray): Long {
        maximumHeight.sort()
        var i = 0
        var j = maximumHeight.size - 1
        while (i < j) {
            var t = maximumHeight[i]
            maximumHeight[i] = maximumHeight[j]
            maximumHeight[j] = t
            i++, j--
        }
        var ans = 0
        var prev = 1e18
        for (h in maximumHeight) {
            var cur = h
            if (cur >= prev) cur = prev - 1
            if (cur <= 0) return -1
            ans += cur
            prev = cur
        }
        return ans
    }
}
