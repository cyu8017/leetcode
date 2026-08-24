// LeetCode 2341 - Maximum Number of Pairs in Array
// https://leetcode.com/problems/maximum-number-of-pairs-in-array/

object Solution {
  def numberOfPairs(nums: Array[Int]): Array[Int] = {
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    nums.foreach(x => cnt(x) = cnt.getOrElse(x, 0) + 1)
    var pairs = 0
    var left = 0
    cnt.values.foreach { c =>
      pairs += c / 2
      left += c % 2
    }
    Array(pairs, left)
  }
}
