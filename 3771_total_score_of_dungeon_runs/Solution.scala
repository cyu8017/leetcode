// LeetCode 3771 - Total Score of Dungeon Runs
// https://leetcode.com/problems/total-score-of-dungeon-runs/

object Solution {
  def totalScore(hp: Int, damage: Array[Int], requirement: Array[Int]): Long = {
    val n = damage.length
    val prefix = new Array[Long](n + 1)
    var i = 0
    while (i < n) {
      prefix(i + 1) = prefix(i) + damage(i)
      i += 1
    }
    var answer = 1L * n * (n + 1) / 2
    var j = 1
    while (j <= n) {
      val threshold = prefix(j) + (requirement(j - 1) - hp)
      var lo = 0
      var hi = j
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (prefix(mid) < threshold) lo = mid + 1
        else hi = mid
      }
      answer -= lo
      j += 1
    }
    answer
  }
}
