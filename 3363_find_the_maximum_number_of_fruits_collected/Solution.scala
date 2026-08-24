// LeetCode 3363 - Find the Maximum Number of Fruits Collected
// https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/

object Solution {
  def maxCollectedFruits(fruits: Array[Array[Int]]): Int = {
    val n = fruits.length
    var ans = 0
    var i = 0
    while (i < n) {
      ans += fruits(i)(i)
      fruits(i)(i) = 0
      i += 1
    }
    val neg = -(1 << 30)
    val dp2 = Array.fill(n, n)(neg)
    val dp3 = Array.fill(n, n)(neg)
    dp2(0)(n - 1) = fruits(0)(n - 1)
    i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        if (dp2(i)(j) != neg) {
          for (dj <- Array(-1, 0, 1)) {
            val ni = i + 1
            val nj = j + dj
            if (ni < n && nj >= 0 && nj < n && nj > ni) {
              val v = dp2(i)(j) + fruits(ni)(nj)
              if (v > dp2(ni)(nj)) dp2(ni)(nj) = v
            }
          }
        }
        j += 1
      }
      i += 1
    }
    dp3(n - 1)(0) = fruits(n - 1)(0)
    var j = 0
    while (j < n) {
      i = 0
      while (i < n) {
        if (dp3(i)(j) != neg) {
          for (di <- Array(-1, 0, 1)) {
            val ni = i + di
            val nj = j + 1
            if (ni >= 0 && ni < n && nj < n && ni > nj) {
              val v = dp3(i)(j) + fruits(ni)(nj)
              if (v > dp3(ni)(nj)) dp3(ni)(nj) = v
            }
          }
        }
        i += 1
      }
      j += 1
    }
    ans += dp2(n - 1)(n - 1) + dp3(n - 1)(n - 1)
    ans
  }
}
