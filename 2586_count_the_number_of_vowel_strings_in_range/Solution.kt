// LeetCode 2586 - Count the Number of Vowel Strings in Range
// https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/

class Solution {
    fun vowelStrings(words: Array<String>, left: Int, right: Int): Int {
        var ans = 0
        for (i in left..right) {
            val w = words[i]
            if (isV(w[0]) && isV(w[w.length - 1])) ans += 1
        }
        return ans
    }

    private fun isV(c: Char): Boolean =
        c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
}
