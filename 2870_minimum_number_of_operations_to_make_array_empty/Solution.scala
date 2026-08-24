// LeetCode 2870 - Minimum Number of Operations to Make Array Empty
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

object Solution {
  def minOperations(nums: Array[Int]): Int = {
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    nums.foreach(v => freq(v) = freq.getOrElse(v, 0) + 1)
    var ans = 0
    freq.values.foreach { c =>
      if (c == 1) return -1
      ans += (c + 2) / 3
    }
    ans
  }
}
