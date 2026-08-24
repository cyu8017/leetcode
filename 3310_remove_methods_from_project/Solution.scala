// LeetCode 3310 - Remove Methods From Project
// https://leetcode.com/problems/remove-methods-from-project/

object Solution {
  def remainingMethods(n: Int, k: Int, invocations: Array[Array[Int]]): Array[Int] = {
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (e <- invocations) g(e(0)) += e(1)
    val sus = new Array[Boolean](n)
    def dfs(u: Int): Unit = {
      if (sus(u)) return
      sus(u) = true
      for (v <- g(u)) dfs(v)
    }
    dfs(k)
    for (e <- invocations) {
      if (!sus(e(0)) && sus(e(1))) return Array.range(0, n)
    }
    (0 until n).filter(!sus(_)).toArray
  }
}
