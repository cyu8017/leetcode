// LeetCode 2746 - Decremental String Concatenation
// https://leetcode.com/problems/decremental-string-concatenation/

object Solution {
  def minimizeConcatenatedLength(words: Array[String]): Int = {
    val n = words.length
    val memo = scala.collection.mutable.Map.empty[String, Int]
    def dfs(i: Int, first: Char, last: Char): Int = {
      if (i == n) return 0
      val key = s"$i,$first,$last"
      if (memo.contains(key)) return memo(key)
      val w = words(i)
      val wf = w.charAt(0)
      val wl = w.charAt(w.length - 1)
      val add1 = w.length - (if (last == wf) 1 else 0)
      val add2 = w.length - (if (wl == first) 1 else 0)
      val a = add1 + dfs(i + 1, first, wl)
      val b = add2 + dfs(i + 1, wf, last)
      val ans = math.min(a, b)
      memo(key) = ans
      ans
    }
    val w0 = words(0)
    w0.length + dfs(1, w0.charAt(0), w0.charAt(w0.length - 1))
  }
}
