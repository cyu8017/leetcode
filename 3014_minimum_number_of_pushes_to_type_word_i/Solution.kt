// LeetCode 3014 - Minimum Number of Pushes to Type Word I
// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

class Solution {
    fun minimumPushes(word: String): Int {
        var n = word.length
        var ans = 0
        var k = 1
        for (i in 0 until n / 8) {
            ans += k * 8
            k++
        }
        ans += k * (n % 8)
        return ans
    }
}
