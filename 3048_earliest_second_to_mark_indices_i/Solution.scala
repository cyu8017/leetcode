// LeetCode 3048 - Earliest Second to Mark Indices I
// https://leetcode.com/problems/earliest-second-to-mark-indices-i/

object Solution {
  def earliestSecondToMarkIndices(nums: Array[Int], changeIndices: Array[Int]): Int = {
    val n = nums.length
    def ok(t: Int): Boolean = {
      val last = Array.ofDim[Int](n + 1)
      var s = 0
      while (s < t) { last(changeIndices(s)) = s; s += 1 }
      var decrement = 0
      var marked = 0
      s = 0
      while (s < t) {
        val i = changeIndices(s)
        if (last(i) == s) {
          if (decrement < nums(i - 1)) return false
          decrement -= nums(i - 1)
          marked += 1
        } else decrement += 1
        s += 1
      }
      marked == n
    }
    val m = changeIndices.length
    var l = 0
    var r = m + 1
    while (l < r) {
      val mid = (l + r) / 2
      if (ok(mid)) r = mid else l = mid + 1
    }
    if (l > m) -1 else l
  }
}
