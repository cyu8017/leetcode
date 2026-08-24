// LeetCode 2155 - All Divisions With the Highest Score of a Binary Array
// https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

object Solution {
  def maxScoreIndices(nums: Array[Int]): List[Int] = {
    val n = nums.length
    var total1 = 0
    nums.foreach(total1 += _)
    var best = total1
    var left0 = 0
    var right1 = total1
    val ans = scala.collection.mutable.ArrayBuffer(0)
    var i = 0
    while (i < n) {
      if (nums(i) == 0) left0 += 1
      else right1 -= 1
      val score = left0 + right1
      if (score > best) {
        best = score
        ans.clear()
        ans += i + 1
      } else if (score == best) ans += i + 1
      i += 1
    }
    ans.toList
  }
}
