// LeetCode 3616 - Number of Student Replacements
// https://leetcode.com/problems/number-of-student-replacements/

object Solution {
  def totalReplacements(ranks: Array[Int]): Int = {
    var ans = 0
    var cur = ranks(0)
    ranks.foreach { x =>
      if (x < cur) {
        cur = x
        ans += 1
      }
    }
    ans
  }
}
