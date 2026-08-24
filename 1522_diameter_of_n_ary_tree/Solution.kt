// LeetCode 1522 - Diameter of N-Ary Tree
// https://leetcode.com/problems/diameter-of-n-ary-tree/

class Node(var `val`: Int) {
    var children: MutableList<Node> = mutableListOf()
}

class Solution {
    private var answer = 0

    fun diameter(root: Node?): Int {
        answer = 0
        if (root != null) depth(root)
        return answer
    }

    private fun depth(node: Node): Int {
        var longest = 0
        var second = 0
        for (child in node.children) {
            val value = depth(child) + 1
            if (value > longest) {
                second = longest
                longest = value
            } else if (value > second) {
                second = value
            }
        }
        answer = maxOf(answer, longest + second)
        return longest
    }
}
