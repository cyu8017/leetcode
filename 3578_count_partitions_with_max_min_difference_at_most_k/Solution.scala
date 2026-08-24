// LeetCode 3578 - Count Partitions With Max-Min Difference at Most K
// https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/

object Solution {
  def countPartitions(nums: Array[Int], k: Int): Int = {
    val mod = 1000000007
    val sl = new java.util.TreeMap[Integer, Integer]()
    val n = nums.length
    val f = new Array[Int](n + 1)
    val g = new Array[Int](n + 1)
    f(0) = 1
    g(0) = 1
    var l = 1
    var r = 1
    while (r <= n) {
      sl.merge(nums(r - 1), 1, (a: Integer, b: Integer) => Integer.valueOf(a + b))
      while (sl.lastKey() - sl.firstKey() > k) {
        val v = nums(l - 1)
        val c = sl.get(v)
        if (c == 1) sl.remove(v)
        else sl.put(v, c - 1)
        l += 1
      }
      f(r) = g(r - 1)
      if (l >= 2) f(r) = (f(r) - g(l - 2) + mod) % mod
      g(r) = (g(r - 1) + f(r)) % mod
      r += 1
    }
    f(n)
  }
}
