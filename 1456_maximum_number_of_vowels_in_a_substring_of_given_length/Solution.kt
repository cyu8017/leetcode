// LeetCode 1456 - Maximum Number of Vowels in a Substring of Given Length
// https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution {
    fun maxVowels(s: String, k: Int): Int {
        val vowels = setOf('a', 'e', 'i', 'o', 'u')
        var cur = s.take(k).count { it in vowels }
        var ans = cur
        for (i in k until s.length) {
            if (s[i] in vowels) cur++
            if (s[i - k] in vowels) cur--
            ans = maxOf(ans, cur)
        }
        return ans
    }
}
