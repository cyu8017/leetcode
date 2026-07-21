// LeetCode 1803 - Count Pairs With XOR in a Range
// https://leetcode.com/problems/count-pairs-with-xor-in-a-range/

class Solution {
    private class TrieNode {
        var count = 0
        val children = arrayOfNulls<TrieNode>(2)
    }

    fun countPairs(nums: IntArray, low: Int, high: Int): Int {
        return countSmallerThan(nums, high + 1) - countSmallerThan(nums, low)
    }

    private fun countSmallerThan(nums: IntArray, limit: Int): Int {
        if (limit <= 0) return 0
        val root = TrieNode()
        var total = 0
        val maxBit = 15
        for (num in nums) {
            total += query(root, num, limit, maxBit)
            insert(root, num, maxBit)
        }
        return total
    }

    private fun insert(root: TrieNode, num: Int, bit: Int) {
        var node = root
        for (i in bit downTo 0) {
            val b = (num shr i) and 1
            if (node.children[b] == null) node.children[b] = TrieNode()
            node = node.children[b]!!
            node.count++
        }
    }

    private fun query(root: TrieNode?, num: Int, limit: Int, bit: Int): Int {
        if (root == null || bit < 0) return 0
        val numBit = (num shr bit) and 1
        val limitBit = (limit shr bit) and 1
        val child = root.children[numBit]
        return if (limitBit == 1) {
            (child?.count ?: 0) + query(root.children[1 - numBit], num, limit, bit - 1)
        } else {
            query(child, num, limit, bit - 1)
        }
    }
}
