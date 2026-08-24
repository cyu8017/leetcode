// LeetCode 0966 - Vowel Spellchecker
// https://leetcode.com/problems/vowel-spellchecker/

class Solution {
    fun spellchecker(wordlist: Array<String>, queries: Array<String>): Array<String> {
        val exact = wordlist.toHashSet()
        val lowerMap = HashMap<String, String>()
        val vowelMap = HashMap<String, String>()
        for (w in wordlist) {
            val low = w.lowercase()
            lowerMap.putIfAbsent(low, w)
            vowelMap.putIfAbsent(devowel(w), w)
        }
        val ans = Array(queries.size) { "" }
        for (i in queries.indices) {
            val q = queries[i]
            ans[i] = when {
                q in exact -> q
                lowerMap.containsKey(q.lowercase()) -> lowerMap[q.lowercase()]!!
                vowelMap.containsKey(devowel(q)) -> vowelMap[devowel(q)]!!
                else -> ""
            }
        }
        return ans
    }

    private fun devowel(w: String): String {
        val chars = w.lowercase().toCharArray()
        for (i in chars.indices) {
            val c = chars[i]
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') chars[i] = '*'
        }
        return String(chars)
    }
}
