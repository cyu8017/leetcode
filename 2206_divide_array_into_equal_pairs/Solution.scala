// LeetCode 2206 - Divide Array Into Equal Pairs
// https://leetcode.com/problems/divide-array-into-equal-pairs/

object Solution {
  def divideArray(nums: Array[Int]): Boolean = {
    val freq = scala.collection.mutable.HashMap.empty[Int, Int]
    for (x <- nums) freq(x) = freq.getOrElse(x, 0) + 1
    freq.values.forall(_ % 2 == 0)
  }
}
