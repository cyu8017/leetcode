// LeetCode 3852 - Smallest Pair With Different Frequencies
// https://leetcode.com/problems/smallest-pair-with-different-frequencies/

object Solution {
  def minDistinctFreqPair(nums: Array[Int]): Array[Int] = {
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    nums.foreach { v => cnt(v) = cnt.getOrElse(v, 0) + 1 }
    var x = nums(0)
    nums.foreach { v => x = math.min(x, v) }
    var minY = Int.MaxValue
    cnt.keys.foreach { y =>
      if (y < minY && cnt(x) != cnt(y)) minY = y
    }
    if (minY == Int.MaxValue) Array(-1, -1)
    else Array(x, minY)
  }
}
