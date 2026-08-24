// LeetCode 2872 - Maximum Number of K-Divisible Components
// https://leetcode.com/problems/maximum-number-of-k-divisible-components/

object Solution {
  private var g: Array[scala.collection.mutable.ArrayBuffer[Int]] = _
  private var values: Array[Int] = _
  private var k: Int = _
  private var ans: Int = _

  def maxKDivisibleComponents(n: Int, edges: Array[Array[Int]], values: Array[Int], k: Int): Int = {
    this.values = values
    this.k = k
    g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    ans = 0
    dfs(0, -1)
    ans
  }

  private def dfs(u: Int, p: Int): Int = {
    var sum = values(u) % k
    g(u).foreach { v =>
      if (v != p) sum = (sum + dfs(v, u)) % k
    }
    if (sum == 0) ans += 1
    sum
  }
}
