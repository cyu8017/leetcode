// LeetCode 3305 - Count of Substrings Containing Every Vowel and K Consonants I
// https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i/

class Solution {
    private fun isVowel(c: Char): Boolean =
        c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'

    private fun atLeast(word: String, k: Int): Int {
        val cnt = HashMap<Char, Int>()
        var cons = 0
        var l = 0
        var ans = 0
        for (r in word.indices) {
            val c = word[r]
            if (isVowel(c)) cnt[c] = (cnt[c] ?: 0) + 1
            else cons++
            while (cnt.size == 5 && cons >= k) {
                ans += word.length - r
                val c2 = word[l]
                if (isVowel(c2)) {
                    val nv = cnt[c2]!! - 1
                    if (nv == 0) cnt.remove(c2) else cnt[c2] = nv
                } else cons--
                l++
            }
        }
        return ans
    }

    fun countOfSubstrings(word: String, k: Int): Int =
        atLeast(word, k) - atLeast(word, k + 1)
}
