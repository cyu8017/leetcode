// LeetCode 2185 - Counting Words With a Given Prefix
// https://leetcode.com/problems/counting-words-with-a-given-prefix/

class Solution {
    fun prefixCount(words: Array<String>, pref: String): Int {
        var ans: Int = 0
        for (w in words)
            if (w.length >= pref.length && w.startsWith(pref)) ans++
        return ans
    }
}
