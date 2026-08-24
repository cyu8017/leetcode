// LeetCode 3669 - Balanced K-Factor Decomposition
// https://leetcode.com/problems/balanced-k-factor-decomposition/

object Solution {
  private val MX = 100001
  private var g: Array[java.util.List[Integer]] = null
  private var inited = false

  private def ensureInit(): Unit = {
    if (inited) return
    g = Array.fill(MX)(new java.util.ArrayList[Integer]())
    var i = 1
    while (i < MX) {
      var j = i
      while (j < MX) {
        g(j).add(i)
        j += i
      }
      i += 1
    }
    inited = true
  }

  def minDifference(n: Int, k: Int): Array[Int] = {
    ensureInit()
    var cur = Int.MaxValue
    var ans = new Array[Int](0)
    val path = new Array[Int](k)

    def dfs(i: Int, x: Int, mi: Int, mx: Int): Unit = {
      if (i == 0) {
        val d = math.max(mx, x) - math.min(mi, x)
        if (d < cur) {
          cur = d
          path(i) = x
          ans = path.clone()
        }
        return
      }
      val it = g(x).iterator()
      while (it.hasNext) {
        val y = it.next().intValue()
        path(i) = y
        dfs(i - 1, x / y, math.min(mi, y), math.max(mx, y))
      }
    }
    dfs(k - 1, n, Int.MaxValue, 0)
    ans
  }
}
