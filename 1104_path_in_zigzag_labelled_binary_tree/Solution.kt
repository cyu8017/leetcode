// LeetCode 1104 - Path In Zigzag Labelled Binary Tree
// https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/

class Solution {
    fun pathInZigZagTree(label: Int): List<Int> {
        var cur = label
        val path = mutableListOf(cur)
        while (cur > 1) {
            val level = 31 - Integer.numberOfLeadingZeros(cur)
            cur = cur shr 1
            cur = (1 shl level) - 1 - cur + (1 shl (level - 1))
            path.add(cur)
        }
        return path.asReversed()
    }
}
