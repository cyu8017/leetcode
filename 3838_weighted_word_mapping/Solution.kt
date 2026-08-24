// LeetCode 3838 - Weighted Word Mapping
// https://leetcode.com/problems/weighted-word-mapping/

class Solution {
    fun mapWordWeights(words: Array<String>, weights: IntArray): String {
        var ans = StringBuilder()
        for (w in words) {
            var s = 0
            for (c in w.toCharArray()) { s = (s + weights[c - 'a']) % 26 }
            ans.append((char) ('a' + (25 - s)))
        }
        return ans.toString()
    }
}
