// LeetCode 2519 - Count the Number of K-Big Indices
// https://leetcode.com/problems/count-the-number-of-k-big-indices/

object Solution {
  private class Fenwick(n: Int) {
    private val bit = new Array[Int](n + 2)
    def add(i0: Int, v: Int): Unit = {
      var i = i0
      while (i < bit.length) {
        bit(i) += v
        i += i & -i
      }
    }
    def sum(i0: Int): Int = {
      var i = i0
      var s = 0
      while (i > 0) {
        s += bit(i)
        i -= i & -i
      }
      s
    }
  }

  def kBigIndices(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val uniq = nums.sorted
    var m = 0
    var i = 0
    while (i < uniq.length) {
      if (i == 0 || uniq(i) != uniq(i - 1)) {
        uniq(m) = uniq(i)
        m += 1
      }
      i += 1
    }
    val rank = scala.collection.mutable.Map.empty[Int, Int]
    i = 0
    while (i < m) {
      rank(uniq(i)) = i + 1
      i += 1
    }
    val left = new Array[Int](n)
    val right = new Array[Int](n)
    var ft = new Fenwick(m)
    i = 0
    while (i < n) {
      val r = rank(nums(i))
      left(i) = ft.sum(r - 1)
      ft.add(r, 1)
      i += 1
    }
    ft = new Fenwick(m)
    i = n - 1
    while (i >= 0) {
      val r = rank(nums(i))
      right(i) = ft.sum(r - 1)
      ft.add(r, 1)
      i -= 1
    }
    var ans = 0
    i = 0
    while (i < n) {
      if (left(i) >= k && right(i) >= k) ans += 1
      i += 1
    }
    ans
  }
}
