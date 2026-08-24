// LeetCode 2554 - Maximum Number of Integers to Choose From a Range I
// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

class Solution {
    fun maxCount(banned: IntArray, n: Int, maxSum: Int): Int {
        val ban = banned.toHashSet()
        var sum = 0L
        var ans = 0
        for (i in 1..n) {
            if (i in ban) continue
            if (sum + i > maxSum) break
            sum += i
            ans += 1
        }
        return ans
    }
}
