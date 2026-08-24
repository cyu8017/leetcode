// LeetCode 3541 - Find Most Frequent Vowel and Consonant
// https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/

class Solution {
    fun maxFreqSum(s: String): Int {
        var cnt = IntArray(26)
        for (c in s.toCharArray()) { cnt[c - 'a']++ }
        var a = 0
        var b = 0
        for (i in 0 until 26) {
            var c = (i + 'a').toInt().toChar()
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
                a = maxOf(a, cnt[i])
            else b = maxOf(b, cnt[i])
        }
        return a + b
    }
}
