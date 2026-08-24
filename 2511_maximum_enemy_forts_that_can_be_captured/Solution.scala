// LeetCode 2511 - Maximum Enemy Forts That Can Be Captured
// https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/

object Solution {
  def captureForts(forts: Array[Int]): Int = {
    var ans = 0
    var prev = -1
    var i = 0
    while (i < forts.length) {
      if (forts(i) != 0) {
        if (prev >= 0 && forts(prev) == -forts(i)) {
          if (i - prev - 1 > ans) ans = i - prev - 1
        }
        prev = i
      }
      i += 1
    }
    ans
  }
}
