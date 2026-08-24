// LeetCode 2279 - Maximum Bags With Full Capacity of Rocks
// https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

object Solution {
  def maximumBags(capacity: Array[Int], rocks: Array[Int], additionalRocks0: Int): Int = {
    val need = new Array[Int](capacity.length)
    var i = 0
    while (i < capacity.length) {
      need(i) = capacity(i) - rocks(i)
      i += 1
    }
    java.util.Arrays.sort(need)
    var additionalRocks = additionalRocks0
    var ans = 0
    for (n <- need) {
      if (additionalRocks < n) return ans
      additionalRocks -= n
      ans += 1
    }
    ans
  }
}
