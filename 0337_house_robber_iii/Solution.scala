// LeetCode 0337 - House Robber III

// https://leetcode.com/problems/house-robber-iii/



class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {

  var value: Int = _value

  var left: TreeNode = _left

  var right: TreeNode = _right

}



object Solution {

  def rob(root: TreeNode): Int = {

    val (withRob, withoutRob) = dfs(root)

    math.max(withRob, withoutRob)

  }



  private def dfs(node: TreeNode): (Int, Int) = {

    if (node == null) {

      return (0, 0)

    }



    val (leftWith, leftWithout) = dfs(node.left)

    val (rightWith, rightWithout) = dfs(node.right)



    val withRob = node.value + leftWithout + rightWithout

    val withoutRob = math.max(leftWith, leftWithout) + math.max(rightWith, rightWithout)

    (withRob, withoutRob)

  }

}
