// LeetCode 1531 - String Compression II
// https://leetcode.com/problems/string-compression-ii/

object Solution {
  def getLengthOfOptimalCompression(s: String, k: Int): Int = {
    val n = s.length
    val memo = scala.collection.mutable.Map.empty[(Int, Int), Int]
    def dp(index: Int, remaining: Int): Int = {
      if (remaining < 0) return 1000000000
      if (index == n || n - index <= remaining) return 0
      memo.getOrElseUpdate((index, remaining), {
        var answer = dp(index + 1, remaining - 1)
        var same = 0
        var removed = 0
        var j = index
        while (j < n) {
          if (s(j) == s(index)) {
            same += 1
            val encoded = 1 + (if (same >= 2) 1 else 0) + (if (same >= 10) 1 else 0) + (if (same >= 100) 1 else 0)
            answer = math.min(answer, encoded + dp(j + 1, remaining - removed))
          } else {
            removed += 1
            if (removed > remaining) { j = n }
          }
          j += 1
        }
        answer
      })
    }
    dp(0, k)
  }
}
