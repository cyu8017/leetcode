// LeetCode 2416 - Sum of Prefix Scores of Strings
// https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

class Solution {
    private class TrieNode {
        val child = arrayOfNulls<TrieNode>(26)
        var cnt = 0
    }

    fun sumPrefixScores(words: Array<String>): IntArray {
        val root = TrieNode()
        for (w in words) {
            var cur = root
            for (ch in w) {
                val c = ch - 'a'
                if (cur.child[c] == null) cur.child[c] = TrieNode()
                cur = cur.child[c]!!
                cur.cnt++
            }
        }
        val ans = IntArray(words.size)
        for (i in words.indices) {
            var cur = root
            var sum = 0
            for (ch in words[i]) {
                cur = cur.child[ch - 'a']!!
                sum += cur.cnt
            }
            ans[i] = sum
        }
        return ans
    }
}
