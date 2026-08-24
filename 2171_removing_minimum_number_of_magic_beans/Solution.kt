// LeetCode 2171 - Removing Minimum Number of Magic Beans
// https://leetcode.com/problems/removing-minimum-number-of-magic-beans/

class Solution {
    fun minimumRemoval(beans: IntArray): Long {
        beans.sort()
        var n: Int = beans.size
        var sum: Long = 0
        for (b in beans) sum += b
        var ans: Long = sum
        for (i in 0 until n) {
            var remain: Long = 1L * (n - i) * beans[i]
            ans = minOf(ans, sum - remain)
        }
        return ans
    }
}
