// LeetCode 2764 - Is Array a Preorder of Some Binary Tree
// https://leetcode.com/problems/is-array-a-preorder-of-some-binary-tree/

class Solution {
    fun isPreorder(nodes: MutableList<MutableList<Int>>): Boolean {
        if (nodes.size == 0) return true
        var stack = ArrayList<Int>()
        stack.add(nodes[0][0])
        for (i in 1 until nodes.size) {
            var id = nodes[i][0]
            var parent = nodes[i][1]
            while (stack.size > 0 && stack[^1] != parent) stack.remove(stack.size - 1)
            if (stack.size == 0) return false
            stack.add(id)
        }
        return true
    }
}
