// LeetCode 3954 - Sum Of Compatible Numbers In Range I
// https://leetcode.com/problems/sum-of-compatible-numbers-in-range-i/

class Solution {
    fun sumOfGoodIntegers(n: Int, k: Int): Int {
        val start = maxOf(1, n - k)
        val end = n + k
        var ans = 0
        for (x in start..end) {
            if ((n and x) == 0) ans += x
        }
        return ans
    }
}
