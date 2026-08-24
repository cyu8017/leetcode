// LeetCode 0337 - House Robber III

// https://leetcode.com/problems/house-robber-iii/



class TreeNode(var `val`: Int) {

    var left: TreeNode? = null

    var right: TreeNode? = null

}



class Solution {

    fun rob(root: TreeNode?): Int {

        val (withRob, withoutRob) = dfs(root)

        return maxOf(withRob, withoutRob)

    }



    private fun dfs(node: TreeNode?): Pair<Int, Int> {

        if (node == null) {

            return 0 to 0

        }



        val (leftWith, leftWithout) = dfs(node.left)

        val (rightWith, rightWithout) = dfs(node.right)



        val withRob = node.`val` + leftWithout + rightWithout

        val withoutRob = maxOf(leftWith, leftWithout) + maxOf(rightWith, rightWithout)

        return withRob to withoutRob

    }

}
