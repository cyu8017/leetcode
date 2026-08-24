// LeetCode 3720 - Lexicographically Smallest Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/

object Solution {
  def lexGreaterPermutation(s: String, target: String): String = {
    val cnt = Array.fill(26)(0)
    s.foreach(c => cnt(c - 'a') += 1)
    val n = s.length
    val ans = new Array[Char](n)

    def dfs(pos: Int, greater: Boolean): Boolean = {
      if (pos == n) return greater
      val start = if (greater) 0 else target.charAt(pos) - 'a'
      var c = start
      while (c < 26) {
        if (cnt(c) != 0) {
          cnt(c) -= 1
          ans(pos) = ('a' + c).toChar
          val ng = greater || c > (target.charAt(pos) - 'a')
          if (dfs(pos + 1, ng)) return true
          cnt(c) += 1
        }
        c += 1
      }
      false
    }

    if (dfs(0, false)) new String(ans) else ""
  }
}
