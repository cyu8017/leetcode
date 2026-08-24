// LeetCode 0421 - Maximum XOR of Two Numbers in an Array
// https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution {
    private class TrieNode(val children: MutableMap<Int, TrieNode> = mutableMapOf())

    fun findMaximumXOR(nums: IntArray): Int {
        val maximum = nums.max()
        val maxBit = if (maximum == 0) 0 else 32 - Integer.numberOfLeadingZeros(maximum)
        val root = TrieNode()
        var best = 0

        for (number in nums) {
            var node = root
            for (bit in maxBit - 1 downTo 0) {
                val current = (number shr bit) and 1
                node = node.children.getOrPut(current) { TrieNode() }
            }
        }

        for (number in nums) {
            var node = root
            var candidate = 0
            for (bit in maxBit - 1 downTo 0) {
                val current = (number shr bit) and 1
                val target = 1 - current
                if (target in node.children) {
                    candidate = candidate or (1 shl bit)
                    node = node.children[target]!!
                } else {
                    node = node.children[current]!!
                }
            }
            best = maxOf(best, candidate)
        }

        return best
    }
}
