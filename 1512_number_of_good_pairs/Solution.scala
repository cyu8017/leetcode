// LeetCode 1512 - Number of Good Pairs
// https://leetcode.com/problems/number-of-good-pairs/

object Solution {
  def numIdenticalPairs(nums: Array[Int]): Int = {
    val counts = scala.collection.mutable.Map.empty[Int, Int]
    var ans = 0
    for (x <- nums) {
      val c = counts.getOrElse(x, 0)
      ans += c
      counts(x) = c + 1
    }
    ans
  }
}
