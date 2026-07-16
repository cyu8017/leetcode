// LeetCode 0255 - Verify Preorder Sequence in Binary Search Tree
// https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/

import scala.collection.mutable

object Solution {
  def verifyPreorder(preorder: Array[Int]): Boolean = {
    var low = Int.MinValue.toLong
    val stack = mutable.ArrayDeque.empty[Int]

    for (value <- preorder) {
      if (value < low) {
        return false
      }
      while (stack.nonEmpty && stack.last < value) {
        low = stack.removeLast()
      }
      stack += value
    }

    true
  }
}
