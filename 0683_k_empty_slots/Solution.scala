// LeetCode 0683 - K Empty Slots
// https://leetcode.com/problems/k-empty-slots/

object Solution {
  def kEmptySlots(bulbs: Array[Int], k: Int): Int = {
    val n = bulbs.length
    val days = Array.ofDim[Int](n)
    var day = 1
    while (day <= n) {
      days(bulbs(day - 1) - 1) = day
      day += 1
    }
    var ans = Int.MaxValue
    var i = 0
    while (i < n - k - 1) {
      val left = i
      val right = i + k + 1
      var j = left + 1
      while (j < right && days(j) > days(left) && days(j) > days(right)) j += 1
      if (j == right) {
        ans = math.min(ans, math.max(days(left), days(right)))
        i += 1
      } else i = j
    }
    if (ans == Int.MaxValue) -1 else ans
  }
}
