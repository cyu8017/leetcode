// LeetCode 3045 - Count Prefix and Suffix Pairs II
// https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/

class Solution {
    class Node {
        var children = HashMap<Int, Node>()
        var cnt = 0
    }

    fun countPrefixSuffixPairs(words: Array<String>): Long {
        var trie = Node()
        var ans = 0
        for (s in words) {
            var node = trie
            var m = s.length
            for (i in 0 until m) {
                var p = s[i] * 32 + s[m - i - 1]
                var next = node.children[p]
                if (next == null) {
                    next = Node()
                    node.children[p] = next
                }
                node = next
                ans += node.cnt
            }
            node.cnt++
        }
        return ans
    }
}
