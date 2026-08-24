// LeetCode 2062 - Count Vowel Substrings of a String
// https://leetcode.com/problems/count-vowel-substrings-of-a-string/

class Solution {
    fun countVowelSubstrings(word: String): Int {
var ans: Int = 0, n = word.length
for (i in 0 until n) {
var seen: HashSet<Char> = HashSet()
for (j in i until n && isVowel(word[j])) {
seen.add(word[j])
if (seen.size == 5) {
ans++
}
}
}
return ans
}

    private fun isVowel(c: Char): Boolean {
return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
}
}
