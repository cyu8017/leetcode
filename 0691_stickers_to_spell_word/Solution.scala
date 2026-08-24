// LeetCode 0691 - Stickers to Spell Word
// https://leetcode.com/problems/stickers-to-spell-word/

object Solution {
  def minStickers(stickers: Array[String], target: String): Int = {
    val need = Array.fill(26)(0)
    for (ch <- target) need(ch - 'a') += 1
    val chars = scala.collection.mutable.ArrayBuffer.empty[Char]
    var i = 0
    while (i < 26) {
      if (need(i) > 0) chars += ('a' + i).toChar
      i += 1
    }
    val sticks = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    for (sticker <- stickers) {
      val counts = Array.fill(26)(0)
      for (ch <- sticker) counts(ch - 'a') += 1
      var useful = false
      for (ch <- chars if counts(ch - 'a') > 0) useful = true
      if (useful) sticks += counts
    }
    val memo = scala.collection.mutable.HashMap.empty[String, Int]
    def key(state: Array[Int]): String = state.mkString(",")
    def dfs(state: Array[Int]): Int = {
      val k = key(state)
      if (memo.contains(k)) return memo(k)
      var idx = 0
      while (idx < state.length && state(idx) == 0) idx += 1
      if (idx == state.length) {
        memo(k) = 0
        return 0
      }
      val first = chars(idx)
      var best = Int.MaxValue / 4
      for (stick <- sticks if stick(first - 'a') != 0) {
        val nxt = state.clone()
        var j = 0
        while (j < chars.length) {
          nxt(j) = math.max(0, nxt(j) - stick(chars(j) - 'a'))
          j += 1
        }
        best = math.min(best, 1 + dfs(nxt))
      }
      memo(k) = best
      best
    }
    val state = Array.tabulate(chars.length)(i => need(chars(i) - 'a'))
    val result = dfs(state)
    if (result >= Int.MaxValue / 4) -1 else result
  }
}
