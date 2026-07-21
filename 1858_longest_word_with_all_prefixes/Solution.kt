// LeetCode 1858 - Longest Word With All Prefixes
// https://leetcode.com/problems/longest-word-with-all-prefixes/

class Solution {
    fun longestWord(words: Array<String>): String {
        val wordSet = words.toHashSet()
        var best = ""
        for (word in words) {
            var prefix = word
            var valid = true
            while (prefix.isNotEmpty()) {
                if (prefix !in wordSet) {
                    valid = false
                    break
                }
                prefix = prefix.dropLast(1)
            }
            if (valid && (word.length > best.length || (word.length == best.length && word < best))) {
                best = word
            }
        }
        return best
    }
}
