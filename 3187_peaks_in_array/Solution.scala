// LeetCode 3187 - Peaks in Array
// https://leetcode.com/problems/peaks-in-array/

object Solution {
  class BIT(n: Int) {
    val c = new Array[Int](n + 1)
    def update(xx: Int, delta: Int): Unit = {
      var x = xx
      while (x <= n) {
        c(x) += delta
        x += x & -x
      }
    }
    def query(xx: Int): Int = {
      var x = xx
      var s = 0
      while (x > 0) {
        s += c(x)
        x -= x & -x
      }
      s
    }
  }

  def countOfPeaks(nums: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val n = nums.length
    val tree = new BIT(n - 1)
    def updatePeak(i: Int, v: Int): Unit = {
      if (i <= 0 || i >= n - 1) return
      if (nums(i - 1) < nums(i) && nums(i) > nums(i + 1)) tree.update(i, v)
    }
    var i = 1
    while (i < n - 1) {
      updatePeak(i, 1)
      i += 1
    }
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (q <- queries) {
      if (q(0) == 1) {
        val l = q(1) + 1
        val r = q(2) - 1
        var t = 0
        if (l <= r) t = tree.query(r) - tree.query(l - 1)
        ans += t
      } else {
        val idx = q(1)
        val v = q(2)
        i = idx - 1
        while (i <= idx + 1) {
          updatePeak(i, -1)
          i += 1
        }
        nums(idx) = v
        i = idx - 1
        while (i <= idx + 1) {
          updatePeak(i, 1)
          i += 1
        }
      }
    }
    ans.toArray
  }
}
