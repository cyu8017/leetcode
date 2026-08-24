// LeetCode 3412 - Find Mirror Score of a String
// https://leetcode.com/problems/find-mirror-score-of-a-string/

object Solution {
  def calculateScore(s: String): Long = {
    val stacks = Array.fill(26)(scala.collection.mutable.ArrayBuffer.empty[Int])
    var ans = 0L
    var i = 0
    while (i < s.length) {
      val ci = s.charAt(i) - 'a'
      val mir = 25 - ci
      if (stacks(mir).nonEmpty) {
        val j = stacks(mir).remove(stacks(mir).length - 1)
        ans += i - j
      } else {
        stacks(ci) += i
      }
      i += 1
    }
    ans
  }
}
