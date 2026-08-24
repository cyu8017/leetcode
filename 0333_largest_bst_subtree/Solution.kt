// LeetCode 0333 - Largest BST Subtree

// https://leetcode.com/problems/largest-bst-subtree/



class TreeNode(var `val`: Int) {

    var left: TreeNode? = null

    var right: TreeNode? = null

}



class Solution {

    private var best = 0



    fun largestBSTSubtree(root: TreeNode?): Int {

        dfs(root)

        return best

    }



    private fun dfs(node: TreeNode?): IntArray {

        if (node == null) {

            return intArrayOf(1, Int.MAX_VALUE, Int.MIN_VALUE, 0)

        }



        val left = dfs(node.left)

        val right = dfs(node.right)



        if (left[0] == 1 && right[0] == 1 && left[2] < node.`val` && right[1] > node.`val`) {

            val size = left[3] + right[3] + 1

            best = maxOf(best, size)

            return intArrayOf(1, minOf(left[1], node.`val`), maxOf(right[2], node.`val`), size)

        }



        return intArrayOf(0, 0, 0, 0)

    }

}
