// LeetCode 3655 - XOR After Range Multiplication Queries II
// https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/

object Solution {
  def xorAfterQueries(nums: Array[Int], queries: Array[Array[Int]]): Int = {
    val MOD = 1000000007
    val n = nums.length
    val byK = new java.util.HashMap[Integer, java.util.List[Array[Int]]]()
    for (q <- queries)
      byK.computeIfAbsent(q(2), _ => new java.util.ArrayList[Array[Int]]()).add(Array(q(0), q(1), q(2), q(3)))
    val res = nums.clone()
    val it = byK.entrySet().iterator()
    while (it.hasNext) {
      val e = it.next()
      val fac = new Array[Int](n)
      java.util.Arrays.fill(fac, 1)
      val uit = e.getValue.iterator()
      while (uit.hasNext) {
        val u = uit.next()
        var i = u(0)
        while (i <= u(1)) {
          fac(i) = ((1L * fac(i) * u(3)) % MOD).toInt
          i += u(2)
        }
      }
      var i = 0
      while (i < n) {
        res(i) = ((1L * res(i) * fac(i)) % MOD).toInt
        i += 1
      }
    }
    var ans = 0
    for (v <- res) ans ^= v
    ans
  }
}
