// LeetCode 2063 - Vowels of All Substrings
// https://leetcode.com/problems/vowels-of-all-substrings/

class Solution {
    fun countVowels(word: String): Long {
var n: Int = word.length
var ans: Long = 0
for (i in 0 until n) {
if (isVowel(word[i])) {
ans += (i + 1).toLong() * (n - i)
}
}
return ans
}

    private fun isVowel(c: Char): Boolean {
return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
}
}
