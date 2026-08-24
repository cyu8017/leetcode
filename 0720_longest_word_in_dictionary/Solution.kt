// LeetCode 0720 - Longest Word in Dictionary
// https://leetcode.com/problems/longest-word-in-dictionary/

class Solution {
    fun longestWord(words: Array<String>): String {
        words.sort()
        var built = HashSet<String>()
        built.add("")
        var best = ""
        for (word in words) {
            if (built.contains(word.substring(0, word.length - 1))) {
                built.add(word)
                if (word.length > best.length) best = word
            }
        }
        return best
    }
}
