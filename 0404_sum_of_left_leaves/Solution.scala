// LeetCode 0404 - Sum of Left Leaves

// https://leetcode.com/problems/sum-of-left-leaves/



class TreeNode(var _value: Int) {

  var value: Int = _value

  var left: TreeNode = null

  var right: TreeNode = null

}



object Solution {

  def sumOfLeftLeaves(root: TreeNode): Int = {

    if (root == null) {

      return 0

    }



    var total = 0



    val left = root.left

    if (left != null && left.left == null && left.right == null) {

      total += left.value

    } else {

      total += sumOfLeftLeaves(left)

    }



    total + sumOfLeftLeaves(root.right)

  }

}
