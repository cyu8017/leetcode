// LeetCode 0536 - Construct Binary Tree from String
// https://leetcode.com/problems/construct-binary-tree-from-string/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    private var index = 0

    fun str2tree(s: String): TreeNode? {
        if (s.isEmpty()) {
            return null
        }
        index = 0
        return parse(s)
    }

    private fun parse(s: String): TreeNode? {
        if (index >= s.length) {
            return null
        }

        var sign = 1
        if (s[index] == '-') {
            sign = -1
            index++
        }

        var value = 0
        while (index < s.length && s[index].isDigit()) {
            value = value * 10 + (s[index] - '0')
            index++
        }

        val node = TreeNode(sign * value)

        if (index < s.length && s[index] == '(') {
            index++
            node.left = parse(s)
            index++
        }

        if (index < s.length && s[index] == '(') {
            index++
            node.right = parse(s)
            index++
        }

        return node
    }
}
