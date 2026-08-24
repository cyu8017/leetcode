// LeetCode 2052 - Minimum Cost to Separate Sentence Into Rows
// https://leetcode.com/problems/minimum-cost-to-separate-sentence-into-rows/

object Solution {
  def minimumCost(sentence: String, k: Int): Int = {
    val words = sentence.trim.split("\\s+")
    val n = words.length
    val INF = 1000000000000000000L
    val dp = Array.fill(n + 1)(INF)
    dp(n) = 0
    var i = n - 1
    while (i >= 0) {
      var length = -1
      var j = i
      var stop = false
      while (!stop && j < n) {
        length += 1 + words(j).length
        if (length > k) stop = true
        else {
          var cost = 0L
          if (j < n - 1) {
            val extra = k - length
            cost = extra.toLong * extra
          }
          dp(i) = math.min(dp(i), cost + dp(j + 1))
          j += 1
        }
      }
      i -= 1
    }
    dp(0).toInt
  }
}
