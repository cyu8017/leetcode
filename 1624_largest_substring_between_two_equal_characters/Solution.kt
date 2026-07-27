// LeetCode 1624 - Largest Substring Between Two Equal Characters
// https://leetcode.com/problems/largest-substring-between-two-equal-characters/

class Solution {
    fun maxLengthBetweenEqualCharacters(s: String): Int {
        val first = HashMap<Char, Int>()
        var ans = -1
        for (i in s.indices) {
            val ch = s[i]
            if (ch in first) ans = maxOf(ans, i - first[ch]!! - 1)
            else first[ch] = i
        }
        return ans
    }
}
