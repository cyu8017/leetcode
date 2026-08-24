// LeetCode 2190 - Most Frequent Number Following Key In an Array
// https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/

object Solution {
  def mostFrequent(nums: Array[Int], key: Int): Int = {
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    var best = 0
    var ans = 0
    var i = 0
    while (i + 1 < nums.length) {
      if (nums(i) == key) {
        freq(nums(i + 1)) = freq.getOrElse(nums(i + 1), 0) + 1
        val v = freq(nums(i + 1))
        if (v > best) { best = v; ans = nums(i + 1) }
      }
      i += 1
    }
    ans
  }
}
