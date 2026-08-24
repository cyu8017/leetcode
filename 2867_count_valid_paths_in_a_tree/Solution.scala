// LeetCode 2867 - Count Valid Paths in a Tree
// https://leetcode.com/problems/count-valid-paths-in-a-tree/

object Solution {
  private var isPrime: Array[Boolean] = _
  private var g: Array[scala.collection.mutable.ArrayBuffer[Int]] = _

  def countPaths(n: Int, edges: Array[Array[Int]]): Long = {
    isPrime = Array.fill(n + 1)(true)
    isPrime(0) = false
    isPrime(1) = false
    var i = 2
    while (i * i <= n) {
      if (isPrime(i)) {
        var j = i * i
        while (j <= n) {
          isPrime(j) = false
          j += i
        }
      }
      i += 1
    }
    g = Array.fill(n + 1)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    var ans = 0L
    for (u <- 1 to n if isPrime(u)) {
      var total = 0L
      g(u).foreach { v =>
        val c = dfs(v, u)
        ans += c
        ans += total * c
        total += c
      }
    }
    ans
  }

  private def dfs(u: Int, p: Int): Int = {
    if (isPrime(u)) return 0
    var sz = 1
    g(u).foreach { v => if (v != p) sz += dfs(v, u) }
    sz
  }
}
