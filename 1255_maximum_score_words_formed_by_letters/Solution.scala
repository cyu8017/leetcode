// LeetCode 1255 - Maximum Score Words Formed by Letters
// https://leetcode.com/problems/maximum-score-words-formed-by-letters/

object Solution {
  def maxScoreWords(words: Array[String], letters: Array[Char], score: Array[Int]): Int = {
    val available = Array.fill(26)(0)
    for (ch <- letters) available(ch - 'a') += 1
    val counts = words.map { w =>
      val c = Array.fill(26)(0)
      for (ch <- w) c(ch - 'a') += 1
      c
    }
    val values = words.map(w => w.map(ch => score(ch - 'a')).sum)
    def canUse(i: Int): Boolean = (0 until 26).forall(j => counts(i)(j) <= available(j))
    def dfs(i: Int): Int = {
      if (i == words.length) return 0
      var best = dfs(i + 1)
      if (canUse(i)) {
        for (j <- 0 until 26) available(j) -= counts(i)(j)
        best = math.max(best, values(i) + dfs(i + 1))
        for (j <- 0 until 26) available(j) += counts(i)(j)
      }
      best
    }
    dfs(0)
  }
}
