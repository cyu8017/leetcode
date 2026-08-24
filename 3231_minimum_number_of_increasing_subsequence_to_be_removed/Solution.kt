// LeetCode 3231 - Minimum Number of Increasing Subsequence to Be Removed
// https://leetcode.com/problems/minimum-number-of-increasing-subsequence-to-be-removed/

class Solution {
    fun minOperations(nums: IntArray): Int {
        val g = ArrayList<Int>()
        for (x in nums) {
            var l = 0
            var r = g.size
            while (l < r) {
                val mid = (l + r) shr 1
                if (g[mid] < x) r = mid
                else l = mid + 1
            }
            if (l == g.size) g.add(x)
            else g[l] = x
        }
        return g.size
    }
}
