// LeetCode 3777 - Minimum Deletions To Make Alternating Substring
// https://leetcode.com/problems/minimum-deletions-to-make-alternating-substring/

object Solution {
  private class BIT(n_ : Int) {
    val n: Int = n_
    val c: Array[Int] = new Array[Int](n_ + 1)
    def update(x0: Int, delta: Int): Unit = {
      var x = x0
      while (x <= n) {
        c(x) += delta
        x += x & -x
      }
    }
    def query(x0: Int): Int = {
      var x = x0
      var s = 0
      while (x > 0) {
        s += c(x)
        x -= x & -x
      }
      s
    }
  }

  def minDeletions(s: String, queries: Array[Array[Int]]): Array[Int] = {
    val n = s.length
    val nums = new Array[Int](n)
    val bit = new BIT(n)
    var i = 1
    while (i < n) {
      if (s.charAt(i) == s.charAt(i - 1)) {
        nums(i) = 1
        bit.update(i + 1, 1)
      }
      i += 1
    }
    val ans = new java.util.ArrayList[Integer]()
    queries.foreach { q =>
      if (q(0) == 1) {
        val j = q(1)
        var delta = (nums(j) ^ 1) - nums(j)
        nums(j) ^= 1
        bit.update(j + 1, delta)
        if (j + 1 < n) {
          delta = (nums(j + 1) ^ 1) - nums(j + 1)
          nums(j + 1) ^= 1
          bit.update(j + 2, delta)
        }
      } else {
        val l = q(1)
        val r = q(2)
        ans.add(bit.query(r + 1) - bit.query(l + 1))
      }
    }
    val out = new Array[Int](ans.size())
    i = 0
    while (i < out.length) {
      out(i) = ans.get(i)
      i += 1
    }
    out
  }
}
