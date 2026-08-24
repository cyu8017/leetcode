// LeetCode 3834 - Merge Adjacent Equal Elements
// https://leetcode.com/problems/merge_adjacent_equal_elements/

object Solution {
  def mergeAdjacent(nums: Array[Int]): Array[Long] = {
    val stk = scala.collection.mutable.ArrayBuffer.empty[Long]
    nums.foreach { x =>
      stk += x.toLong
      while (stk.length > 1 && stk(stk.length - 1) == stk(stk.length - 2)) {
        val a = stk.remove(stk.length - 1)
        val b = stk.remove(stk.length - 1)
        stk += a + b
      }
    }
    stk.toArray
  }
}
