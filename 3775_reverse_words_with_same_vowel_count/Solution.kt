// LeetCode 3775 - Reverse Words With Same Vowel Count
// https://leetcode.com/problems/reverse_words_with_same_vowel_count/

class Solution {
    private fun calc(w: String): Int {
        var cnt = 0
        for (c in w) {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') cnt++
        }
        return cnt
    }

    fun reverseWords(s: String): String {
        val words = s.trim().split("\\s+".toRegex())
        val cnt = calc(words[0])
        val ans = StringBuilder()
        ans.append(words[0])
        for (i in 1 until words.size) {
            var w = words[i]
            if (calc(w) == cnt) w = w.reversed()
            ans.append(' ').append(w)
        }
        return ans.toString()
    }
}
