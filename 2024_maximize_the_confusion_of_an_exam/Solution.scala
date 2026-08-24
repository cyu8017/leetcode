// LeetCode 2024 - Maximize the Confusion of an Exam
// https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

object Solution {
  def maxConsecutiveAnswers(answerKey: String, k: Int): Int = {
    math.max(maxWith(answerKey, k, 'T'), maxWith(answerKey, k, 'F'))
  }

  private def maxWith(answerKey: String, k: Int, ch: Char): Int = {
    var left = 0
    var bad = 0
    var best = 0
    var right = 0
    while (right < answerKey.length) {
      if (answerKey.charAt(right) != ch) bad += 1
      while (bad > k) {
        if (answerKey.charAt(left) != ch) bad -= 1
        left += 1
      }
      best = math.max(best, right - left + 1)
      right += 1
    }
    best
  }
}
