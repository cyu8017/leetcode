// LeetCode 3354 - Make Array Elements Equal to Zero
// https://leetcode.com/problems/make-array-elements-equal-to-zero/

object Solution {
  def countValidSelections(nums: Array[Int]): Int = {
    val n = nums.length
    var ans = 0
    var i = 0
    while (i < n) {
      if (nums(i) == 0) {
        for (dir <- Array(-1, 1)) {
          val a = nums.clone()
          var cur = i
          var d = dir
          while (cur >= 0 && cur < n) {
            if (a(cur) == 0) cur += d
            else {
              a(cur) -= 1
              d = -d
              cur += d
            }
          }
          var ok = true
          for (v <- a) if (v != 0) ok = false
          if (ok) ans += 1
        }
      }
      i += 1
    }
    ans
  }
}
