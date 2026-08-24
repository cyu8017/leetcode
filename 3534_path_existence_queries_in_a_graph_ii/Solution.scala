// LeetCode 3534 - Path Existence Queries in a Graph II
// https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/

object Solution {
  def pathExistenceQueries(n: Int, nums: Array[Int], maxDiff: Int, queries: Array[Array[Int]]): Array[Int] = {
    val pairs = Array.ofDim[Int](n, 2)
    var i = 0
    while (i < n) { pairs(i) = Array(nums(i), i); i += 1 }
    java.util.Arrays.sort(pairs, (a: Array[Int], b: Array[Int]) => Integer.compare(a(0), b(0)))
    val m = 20
    val f = Array.ofDim[Int](n, m)
    var r = n - 1
    var l = n - 1
    while (l >= 0) {
      while (pairs(r)(0) - pairs(l)(0) > maxDiff) r -= 1
      i = pairs(l)(1)
      val j = pairs(r)(1)
      f(i)(0) = j
      var k = 1
      while (k < m) { f(i)(k) = f(f(i)(k - 1))(k - 1); k += 1 }
      l -= 1
    }
    val ans = new java.util.ArrayList[Integer]()
    for (q <- queries) {
      var ii = q(0)
      var jj = q(1)
      if (nums(ii) > nums(jj)) { val tmp = ii; ii = jj; jj = tmp }
      if (ii == jj) ans.add(0)
      else if (nums(ii) == nums(jj)) ans.add(1)
      else {
        var d = 0
        var k = m - 1
        while (k >= 0) {
          if (nums(f(ii)(k)) < nums(jj)) {
            d |= 1 << k
            ii = f(ii)(k)
          }
          k -= 1
        }
        if (nums(f(ii)(0)) < nums(jj)) ans.add(-1)
        else ans.add(d + 1)
      }
    }
    val out = new Array[Int](ans.size())
    var t = 0
    while (t < ans.size()) { out(t) = ans.get(t); t += 1 }
    out
  }
}
