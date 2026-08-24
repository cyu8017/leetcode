// LeetCode 3663 - Find The Least Frequent Digit
// https://leetcode.com/problems/find-the-least-frequent-digit/

class Solution {
    fun getLeastFrequentDigit(n: Int): Int {
        var cnt = IntArray(10)
        var ans = 0
        var f = 1  shl  30
        for (; n > 0; n /= 10) cnt[n % 10]++
        for (x in 0 until 10) {
            if (cnt[x] > 0 && cnt[x] < f) {
                f = cnt[x]
                ans = x
            }
        }
        return ans
    }
}
