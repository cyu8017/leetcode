// LeetCode 3366 - Minimum Array Sum
// https://leetcode.com/problems/minimum-array-sum/

object Solution {
  def minArraySum(nums: Array[Int], k: Int, op1: Int, op2: Int): Int = {
    val inf = 1000000000000000000L
    var dp = Array.fill(op1 + 1, op2 + 1)(inf)
    dp(0)(0) = 0
    def tryCand(ndp: Array[Array[Long]], base: Long, na: Int, nb: Int, v: Int): Unit = {
      if (base + v < ndp(na)(nb)) ndp(na)(nb) = base + v
    }
    for (x <- nums) {
      val ndp = Array.fill(op1 + 1, op2 + 1)(inf)
      var a = 0
      while (a <= op1) {
        var b = 0
        while (b <= op2) {
          if (dp(a)(b) != inf) {
            tryCand(ndp, dp(a)(b), a, b, x)
            if (a < op1) tryCand(ndp, dp(a)(b), a + 1, b, (x + 1) / 2)
            if (b < op2 && x >= k) tryCand(ndp, dp(a)(b), a, b + 1, x - k)
            if (a < op1 && b < op2) {
              val v1 = (x + 1) / 2
              if (v1 >= k) tryCand(ndp, dp(a)(b), a + 1, b + 1, v1 - k)
              if (x >= k) tryCand(ndp, dp(a)(b), a + 1, b + 1, (x - k + 1) / 2)
            }
          }
          b += 1
        }
        a += 1
      }
      dp = ndp
    }
    var ans = inf
    var a = 0
    while (a <= op1) {
      var b = 0
      while (b <= op2) {
        if (dp(a)(b) < ans) ans = dp(a)(b)
        b += 1
      }
      a += 1
    }
    ans.toInt
  }
}
