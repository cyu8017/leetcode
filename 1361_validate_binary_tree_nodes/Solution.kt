// LeetCode 1361 - Validate Binary Tree Nodes
// https://leetcode.com/problems/validate-binary-tree-nodes/

class Solution {
    fun validateBinaryTreeNodes(n: Int, leftChild: IntArray, rightChild: IntArray): Boolean {
        val indeg = IntArray(n)
        for (x in leftChild + rightChild) {
            if (x != -1) {
                indeg[x]++
                if (indeg[x] > 1) return false
            }
        }
        val roots = indeg.indices.filter { indeg[it] == 0 }
        if (roots.size != 1) return false
        val seen = HashSet<Int>()
        val stack = ArrayDeque<Int>()
        stack.add(roots[0])
        while (stack.isNotEmpty()) {
            val u = stack.removeLast()
            if (!seen.add(u)) return false
            for (v in intArrayOf(leftChild[u], rightChild[u])) {
                if (v != -1) stack.add(v)
            }
        }
        return seen.size == n
    }
}
