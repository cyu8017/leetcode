// LeetCode 3068 - Find the Maximum Sum of Node Values
// https://leetcode.com/problems/find-the-maximum-sum-of-node-values/

object Solution {
  def maximumValueSum(nums: Array[Int], k: Int, edges: Array[Array[Int]]): Long = {
    var f0 = 0L
    var f1 = -0x3f3f3f3fL
    nums.foreach { x =>
      val nf0 = math.max(f0 + x, f1 + (x ^ k))
      val nf1 = math.max(f1 + x, f0 + (x ^ k))
      f0 = nf0
      f1 = nf1
    }
    f0
  }
}
