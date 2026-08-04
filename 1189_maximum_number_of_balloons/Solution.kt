// LeetCode 1189 - Maximum Number of Balloons
// https://leetcode.com/problems/maximum-number-of-balloons/

class Solution {
    fun maxNumberOfBalloons(text: String): Int {
        val count = IntArray(26)
        for (c in text) count[c - 'a']++
        return minOf(count[1], count[0], count[11] / 2, count[14] / 2, count[13])
    }
}
