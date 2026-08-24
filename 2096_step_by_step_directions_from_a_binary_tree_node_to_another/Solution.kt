// LeetCode 2096 - Step-By-Step Directions From a Binary Tree Node to Another
// https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    private fun path(node: TreeNode?, target: Int, p: StringBuilder): Boolean {
        if (node == null) return false
        if (node.`val` == target) return true
        p.append('L')
        if (path(node.left, target, p)) return true
        p.setCharAt(p.length - 1, 'R')
        if (path(node.right, target, p)) return true
        p.setLength(p.length - 1)
        return false
    }

    fun getDirections(root: TreeNode?, startValue: Int, destValue: Int): String {
        val ps = StringBuilder()
        val pd = StringBuilder()
        path(root, startValue, ps)
        path(root, destValue, pd)
        var i = 0
        while (i < ps.length && i < pd.length && ps[i] == pd[i]) i++
        val ans = StringBuilder()
        repeat(ps.length - i) { ans.append('U') }
        ans.append(pd.substring(i))
        return ans.toString()
    }
}
