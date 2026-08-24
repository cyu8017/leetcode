// LeetCode 3251 - Find the Count of Monotonic Pairs II
// https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/

object Solution {
  def countOfPairs(nums: Array[Int]): Int = {
    val mod = 1000000007
    val n = nums.length
    var maxV = 0
    for (v <- nums) maxV = math.max(maxV, v)
    var dp = new Array[Int](maxV + 1)
    var a = 0
    while (a <= nums(0)) { dp(a) = 1; a += 1 }
    var i = 1
    while (i < n) {
      val ndp = new Array[Int](maxV + 1)
      val pref = new Array[Int](maxV + 2)
      a = 0
      while (a <= maxV) { pref(a + 1) = (pref(a) + dp(a)) % mod; a += 1 }
      var a2 = 0
      while (a2 <= nums(i)) {
        val b2 = nums(i) - a2
        var maxA1 = a2
        val lim = nums(i - 1) - b2
        if (lim < maxA1) maxA1 = lim
        if (maxA1 >= 0) {
          if (maxA1 > maxV) maxA1 = maxV
          ndp(a2) = pref(maxA1 + 1)
        }
        a2 += 1
      }
      dp = ndp
      i += 1
    }
    var ans = 0
    for (v <- dp) ans = (ans + v) % mod
    ans
  }
}
