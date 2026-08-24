// LeetCode 1530 - Number of Good Leaf Nodes Pairs
// https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    private var answer = 0

    fun countPairs(root: TreeNode?, distance: Int): Int {
        answer = 0
        dfs(root, distance)
        return answer
    }

    private fun dfs(node: TreeNode?, distance: Int): List<Int> {
        if (node == null) return emptyList()
        if (node.left == null && node.right == null) return listOf(1)
        val left = dfs(node.left, distance)
        val right = dfs(node.right, distance)
        for (a in left) {
            for (b in right) {
                if (a + b <= distance) answer++
            }
        }
        val depths = mutableListOf<Int>()
        for (depth in left) {
            if (depth + 1 < distance) depths.add(depth + 1)
        }
        for (depth in right) {
            if (depth + 1 < distance) depths.add(depth + 1)
        }
        return depths
    }
}
