// LeetCode 1849 - Splitting a String Into Descending Consecutive Values
// https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

object Solution {
  def splitString(s: String): Boolean = {
    val n = s.length

    def dfs(index: Int, previous: Option[BigInt], parts: Int): Boolean = {
      if (index == n) return parts >= 2
      var end = index + 1
      while (end <= n) {
        val value = BigInt(s.substring(index, end))
        previous match {
          case None =>
            if (dfs(end, Some(value), parts + 1)) return true
          case Some(prev) =>
            if (value == prev - 1) {
              if (dfs(end, Some(value), parts + 1)) return true
            } else if (value > prev - 1) return false
        }
        end += 1
      }
      false
    }

    dfs(0, None, 0)
  }
}
