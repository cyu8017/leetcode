// LeetCode 0851 - Loud and Rich
// https://leetcode.com/problems/loud-and-rich/

object Solution {
  def loudAndRich(richer: Array[Array[Int]], quiet: Array[Int]): Array[Int] = {
    val n = quiet.length
    val graph = Array.fill(n)(scala.collection.mutable.ListBuffer.empty[Int])
    richer.foreach { e => graph(e(1)) += e(0) }
    val ans = Array.fill(n)(-1)
    def dfs(person: Int): Int = {
      if (ans(person) != -1) return ans(person)
      var best = person
      graph(person).foreach { richerPerson =>
        val cand = dfs(richerPerson)
        if (quiet(cand) < quiet(best)) best = cand
      }
      ans(person) = best
      best
    }
    (0 until n).foreach(dfs)
    ans
  }
}
