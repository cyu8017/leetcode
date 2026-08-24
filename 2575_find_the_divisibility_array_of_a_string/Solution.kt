// LeetCode 2575 - Find the Divisibility Array of a String
// https://leetcode.com/problems/find-the-divisibility-array-of-a-string/

class Solution {
    fun divisibilityArray(word: String, m: Int): IntArray {
        var ans = IntArray(word.length)
        var cur = 0
        for (i in 0 until word.length) {
            cur = (cur * 10 + (word[i] - '0')) % m
            if (cur == 0) ans[i] = 1
        }
        return ans
    }
}
