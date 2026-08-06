// LeetCode 1208 - Get Equal Substrings Within Budget
// https://leetcode.com/problems/get-equal-substrings-within-budget/

object Solution {
  def equalSubstring(s: String, t: String, maxCost: Int): Int = {
    var left = 0
    var cost = 0
    var answer = 0
    for (right <- s.indices) {
      cost += math.abs(s(right) - t(right))
      while (cost > maxCost) {
        cost -= math.abs(s(left) - t(left))
        left += 1
      }
      answer = math.max(answer, right - left + 1)
    }
    answer
  }
}
