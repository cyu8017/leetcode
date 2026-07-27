// LeetCode 1698 - Number of Distinct Substrings in a String
// https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/

class Solution {
    fun countDistinct(s: String): Int {
        class TrieNode {
            val children = HashMap<Char, TrieNode>()
        }
        val root = TrieNode()
        var ans = 0
        for (i in s.indices) {
            var node = root
            for (j in i until s.length) {
                val c = s[j]
                val next = node.children[c]
                if (next == null) {
                    val created = TrieNode()
                    node.children[c] = created
                    ans++
                    node = created
                } else {
                    node = next
                }
            }
        }
        return ans
    }
}
