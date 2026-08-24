// LeetCode 3761 - Minimum Absolute Distance Between Mirror Pairs
// https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/

object Solution {
  def minMirrorPairDistance(nums: Array[Int]): Int = {
    val n = nums.length
    val pos = new java.util.HashMap[Integer, Integer]()
    var ans = n + 1
    var i = 0
    while (i < n) {
      if (pos.containsKey(nums(i))) ans = math.min(ans, i - pos.get(nums(i)))
      pos.put(reverse(nums(i)), i)
      i += 1
    }
    if (ans > n) -1 else ans
  }

  private def reverse(x0: Int): Int = {
    var x = x0
    var y = 0
    while (x > 0) {
      y = y * 10 + x % 10
      x /= 10
    }
    y
  }
}
