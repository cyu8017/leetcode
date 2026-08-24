// LeetCode 2638 - Count the Number of K-Free Subsets
// https://leetcode.com/problems/count-the-number-of-k-free-subsets/

object Solution {
  def countTheNumOfKFreeSubsets(nums: Array[Int], k: Int): Long = {
    val sorted = nums.sorted
    val groups = scala.collection.mutable.LinkedHashMap.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]
    var i = 0
    while (i < sorted.length) {
      val x = sorted(i)
      groups.getOrElseUpdate(x % k, scala.collection.mutable.ArrayBuffer.empty[Int]) += x
      i += 1
    }
    var ans = 1L
    groups.values.foreach { g =>
      var prevVal = -1
      var prevTake = 0L
      var prevSkip = 1L
      g.foreach { v =>
        val skip = prevTake + prevSkip
        val take = if (prevVal + k == v) prevSkip else prevTake + prevSkip
        prevTake = take
        prevSkip = skip
        prevVal = v
      }
      ans *= prevTake + prevSkip
    }
    ans
  }
}
