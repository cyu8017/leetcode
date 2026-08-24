// LeetCode 0697 - Degree of an Array
// https://leetcode.com/problems/degree-of-an-array/

object Solution {
  def findShortestSubArray(nums: Array[Int]): Int = {
    val first = scala.collection.mutable.HashMap.empty[Int, Int]
    val last = scala.collection.mutable.HashMap.empty[Int, Int]
    val count = scala.collection.mutable.HashMap.empty[Int, Int]
    var i = 0
    while (i < nums.length) {
      if (!first.contains(nums(i))) first(nums(i)) = i
      last(nums(i)) = i
      count(nums(i)) = count.getOrElse(nums(i), 0) + 1
      i += 1
    }
    var degree = 0
    for (freq <- count.values) degree = math.max(degree, freq)
    var best = Int.MaxValue
    for ((key, freq) <- count if freq == degree) {
      best = math.min(best, last(key) - first(key) + 1)
    }
    best
  }
}
