// LeetCode 3656 - Determine if a Simple Graph Exists
// https://leetcode.com/problems/determine-if-a-simple-graph-exists/

object Solution {
  def simpleGraphExists(degrees: Array[Int]): Boolean = {
    val n = degrees.length
    val d = degrees.clone()
    java.util.Arrays.sort(d)
    var i = 0
    var j = n - 1
    while (i < j) {
      val tmp = d(i)
      d(i) = d(j)
      d(j) = tmp
      i += 1
      j -= 1
    }
    var sum = 0L
    for (x <- d) {
      if (x < 0 || x >= n) return false
      sum += x
    }
    if (sum % 2 == 1) return false
    val prefix = new Array[Long](n + 1)
    i = 0
    while (i < n) {
      prefix(i + 1) = prefix(i) + d(i)
      i += 1
    }
    var k = 1
    while (k <= n) {
      var right = 0L
      i = k
      while (i < n) {
        right += (if (d(i) < k) d(i) else k)
        i += 1
      }
      if (prefix(k) > 1L * k * (k - 1) + right) return false
      k += 1
    }
    true
  }
}
