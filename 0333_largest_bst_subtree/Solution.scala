// LeetCode 0333 - Largest BST Subtree

// https://leetcode.com/problems/largest-bst-subtree/



class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {

  var value: Int = _value

  var left: TreeNode = _left

  var right: TreeNode = _right

}



object Solution {

  private var best = 0



  def largestBSTSubtree(root: TreeNode): Int = {

    best = 0

    dfs(root)

    best

  }



  private def dfs(node: TreeNode): (Boolean, Int, Int, Int) = {

    if (node == null) {

      return (true, Int.MaxValue, Int.MinValue, 0)

    }



    val (leftOk, leftMin, leftMax, leftSize) = dfs(node.left)

    val (rightOk, rightMin, rightMax, rightSize) = dfs(node.right)



    if (leftOk && rightOk && leftMax < node.value && rightMin > node.value) {

      val size = leftSize + rightSize + 1

      best = math.max(best, size)

      (true, math.min(leftMin, node.value), math.max(rightMax, node.value), size)

    } else {

      (false, 0, 0, 0)

    }

  }

}
