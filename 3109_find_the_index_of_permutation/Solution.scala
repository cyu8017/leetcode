// LeetCode 3109 - Find the Index of Permutation
// https://leetcode.com/problems/find-the-index-of-permutation/

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

  def getPermutationIndex(perm: Array[Int]): Int = {
    val MOD = 1000000007
    val n = perm.length
    val tree = new BIT(n + 1)
    val f = new Array[Int](n)
    f(0) = 1
    var i = 1
    while (i < n) {
      f(i) = ((f(i - 1).toLong * i) % MOD).toInt
      i += 1
    }
    var ans = 0L
    i = 0
    while (i < n) {
      val x = perm(i)
      val cnt = x - 1 - tree.query(x)
      ans = (ans + cnt.toLong * f(n - 1 - i)) % MOD
      tree.update(x, 1)
      i += 1
    }
    ans.toInt
  }
}
