// LeetCode 3185 - Count Pairs That Form a Complete Day II
// https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/

object Solution {
  def countCompleteDayPairs(hours: Array[Int]): Long = {
    val cnt = new Array[Int](24)
    var ans = 0L
    for (x <- hours) {
      ans += cnt((24 - x % 24) % 24)
      cnt(x % 24) += 1
    }
    ans
  }
}
