// LeetCode 2261 - K Divisible Elements Subarrays
// https://leetcode.com/problems/k-divisible-elements-subarrays/

object Solution {
  def countDistinct(nums: Array[Int], k: Int, p: Int): Int = {
    val n = nums.length
    val seen = scala.collection.mutable.HashSet.empty[String]
    var i = 0
    while (i < n) {
      var div = 0
      val key = new StringBuilder
      var j = i
      while (j < n) {
        if (nums(j) % p == 0) div += 1
        if (div > k) {
          j = n
        } else {
          key.append(nums(j) + 1).append(',')
          seen += key.toString
          j += 1
        }
      }
      i += 1
    }
    seen.size
  }
}
