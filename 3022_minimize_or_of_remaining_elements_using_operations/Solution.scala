// LeetCode 3022 - Minimize OR of Remaining Elements Using Operations
// https://leetcode.com/problems/minimize-or-of-remaining-elements-using-operations/

object Solution {
  def minOrAfterOperations(nums: Array[Int], k: Int): Int = {
    var ans = 0
    var rans = 0
    var i = 29
    while (i >= 0) {
      val test = ans + (1 << i)
      var cnt = 0
      var value = 0
      for (num <- nums) {
        if (value == 0) value = test & num
        else value &= test & num
        if (value != 0) cnt += 1
      }
      if (cnt > k) rans += (1 << i)
      else ans += (1 << i)
      i -= 1
    }
    rans
  }
}
