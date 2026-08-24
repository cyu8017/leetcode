// LeetCode 3640 - Trionic Array II
// https://leetcode.com/problems/trionic-array-ii/

object Solution {
  def maxSumTrionic(nums: Array[Int]): Long = {
    val n = nums.length
    var i = 0
    var ans = Long.MinValue
    while (i < n) {
      val l = i
      i += 1
      while (i < n && nums(i - 1) < nums(i)) i += 1
      if (i != l + 1) {
        val p = i - 1
        var s = nums(p - 1).toLong + nums(p)
        while (i < n && nums(i - 1) > nums(i)) {
          s += nums(i)
          i += 1
        }
        if (!(i == p + 1 || i == n || nums(i - 1) == nums(i))) {
          val q = i - 1
          s += nums(i)
          i += 1
          var mx = 0L
          var t = 0L
          while (i < n && nums(i - 1) < nums(i)) {
            t += nums(i)
            i += 1
            mx = math.max(mx, t)
          }
          s += mx
          mx = 0
          t = 0
          var j = p - 2
          while (j >= l) {
            t += nums(j)
            mx = math.max(mx, t)
            j -= 1
          }
          s += mx
          ans = math.max(ans, s)
          i = q
        }
      }
    }
    ans
  }
}
