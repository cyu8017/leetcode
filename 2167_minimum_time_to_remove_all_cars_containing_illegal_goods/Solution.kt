// LeetCode 2167 - Minimum Time to Remove All Cars Containing Illegal Goods
// https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/

class Solution {
    fun minimumTime(s: String): Int {
        var n: Int = s.length
        var left: IntArray = IntArray(n)
        if (s[0] == '1') left[0] = 1
        for (i in 1 until n) {
            left[i] = left[i - 1]
            if (s[i] == '1') left[i] = minOf(i + 1, left[i - 1] + 2)
        }
        var ans: Int = left[n - 1], right = 0
        for (i in n - 1 downTo 0) {
            if (s[i] == '1') right = minOf(n - i, right + 2)
            var leftCost: Int = if (i > 0) left[i - 1] else 0
            ans = minOf(ans, leftCost + right)
        }
        return ans
    }
}
