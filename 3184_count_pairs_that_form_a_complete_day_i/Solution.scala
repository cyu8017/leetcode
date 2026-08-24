// LeetCode 3184 - Count Pairs That Form a Complete Day I
// https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/

object Solution {
  def countCompleteDayPairs(hours: Array[Int]): Int = {
    val cnt = new Array[Int](24)
    var ans = 0
    for (x <- hours) {
      ans += cnt((24 - x % 24) % 24)
      cnt(x % 24) += 1
    }
    ans
  }
}
