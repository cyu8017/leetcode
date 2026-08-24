// LeetCode 0404 - Sum of Left Leaves

// https://leetcode.com/problems/sum-of-left-leaves/



class TreeNode(var `val`: Int) {

    var left: TreeNode? = null

    var right: TreeNode? = null

}



class Solution {

    fun sumOfLeftLeaves(root: TreeNode?): Int {

        if (root == null) {

            return 0

        }



        var total = 0



        val left = root.left

        if (left != null && left.left == null && left.right == null) {

            total += left.`val`

        } else {

            total += sumOfLeftLeaves(left)

        }



        total += sumOfLeftLeaves(root.right)



        return total

    }

}
