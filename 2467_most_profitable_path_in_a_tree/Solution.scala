// LeetCode 2467 - Most Profitable Path in a Tree
// https://leetcode.com/problems/most-profitable-path-in-a-tree/

object Solution {
  def mostProfitablePath(edges: Array[Array[Int]], bob: Int, amount: Array[Int]): Int = {
    val n = amount.length
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    val bobTime = Array.fill(n)(n)

    def findBob(u: Int, p: Int, t: Int): Boolean = {
      if (u == 0) {
        bobTime(u) = t
        return true
      }
      g(u).foreach { v =>
        if (v != p && findBob(v, u, t + 1)) {
          bobTime(u) = t
          return true
        }
      }
      false
    }

    findBob(bob, -1, 0)
    var ans = Int.MinValue

    def dfs(u: Int, p: Int, t: Int, income0: Int): Unit = {
      var cur = amount(u)
      if (t > bobTime(u)) cur = 0
      else if (t == bobTime(u)) cur /= 2
      val income = income0 + cur
      var isLeaf = true
      g(u).foreach { v =>
        if (v != p) {
          isLeaf = false
          dfs(v, u, t + 1, income)
        }
      }
      if (isLeaf && income > ans) ans = income
    }

    dfs(0, -1, 0, 0)
    ans
  }
}
