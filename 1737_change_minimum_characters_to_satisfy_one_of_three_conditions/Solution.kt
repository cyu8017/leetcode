// LeetCode 1737 - Change Minimum Characters to Satisfy One of Three Conditions
// https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/

class Solution {
    fun minCharacters(a: String, b: String): Int {
        val ca = IntArray(26)
        val cb = IntArray(26)
        for (ch in a) {
            ca[ch - 'a']++
        }
        for (ch in b) {
            cb[ch - 'a']++
        }
        val n = a.length
        val m = b.length
        val maxCount = maxOf(ca.max(), cb.max())
        var ans = n + m - maxCount
        var preA = 0
        var preB = 0
        for (code in 0 until 25) {
            preA += ca[code]
            preB += cb[code]
            ans = minOf(ans, n - preA + preB, m - preB + preA)
        }
        return ans
    }
}
