// LeetCode 3728 - Stable Subarrays With Equal Boundary And Interior Sum
// https://leetcode.com/problems/stable-subarrays-with-equal-boundary-and-interior-sum/

object Solution {
  def countStableSubarrays(capacity: Array[Int]): Long = {
    val n = capacity.length
    val s = new Array[Long](n + 1)
    var i = 1
    while (i <= n) {
      s(i) = s(i - 1) + capacity(i - 1)
      i += 1
    }
    val cnt = new java.util.HashMap[String, Integer]()
    var ans = 0L
    var r = 2
    while (r < n) {
      val l = r - 2
      val keyL = capacity(l) + "#" + (capacity(l) + s(l + 1))
      cnt.merge(keyL, 1, (a: Integer, b: Integer) => Integer.valueOf(a + b))
      val keyR = capacity(r) + "#" + s(r)
      ans += cnt.getOrDefault(keyR, 0)
      r += 1
    }
    ans
  }
}
