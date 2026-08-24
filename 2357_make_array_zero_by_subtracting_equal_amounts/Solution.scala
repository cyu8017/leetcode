// LeetCode 2357 - Make Array Zero by Subtracting Equal Amounts
// https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

object Solution {
  def minimumOperations(nums: Array[Int]): Int = {
    val seen = scala.collection.mutable.HashSet.empty[Int]
    nums.foreach(x => if (x > 0) seen += x)
    seen.size
  }
}
