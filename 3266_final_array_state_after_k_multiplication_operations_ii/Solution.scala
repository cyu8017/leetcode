// LeetCode 3266 - Final Array State After K Multiplication Operations II
// https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/

object Solution {
  def modPow(a0: Long, e0: Long, mod: Long): Long = {
    var r = 1L
    var a = a0 % mod
    var e = e0
    while (e > 0) {
      if ((e & 1) != 0) r = r * a % mod
      a = a * a % mod
      e >>= 1
    }
    r
  }

  def getFinalState(nums: Array[Int], k0: Int, multiplier: Int): Array[Int] = {
    val mod = 1000000007
    if (multiplier == 1) return nums
    val h = new java.util.PriorityQueue[Array[Int]]((a: Array[Int], b: Array[Int]) =>
      if (a(0) != b(0)) Integer.compare(a(0), b(0)) else Integer.compare(a(1), b(1))
    )
    var maxV = 0
    var i = 0
    while (i < nums.length) {
      h.offer(Array(nums(i), i))
      if (nums(i) > maxV) maxV = nums(i)
      i += 1
    }
    var k = k0
    var stop = false
    while (k > 0 && !h.isEmpty && !stop) {
      val cur = h.poll()
      val v = cur(0)
      val idx = cur(1)
      if (v.toLong * multiplier > maxV && k >= nums.length) {
        h.offer(Array(v, idx))
        stop = true
      } else {
        val nv = v * multiplier
        nums(idx) = nv
        if (nv > maxV) maxV = nv
        h.offer(Array(nv, idx))
        k -= 1
      }
    }
    if (k > 0) {
      val n = nums.length
      val full = k / n
      val rem = k % n
      val powFull = modPow(multiplier.toLong, full.toLong, mod)
      i = 0
      while (i < n) {
        nums(i) = ((nums(i).toLong * powFull) % mod).toInt
        i += 1
      }
      val hh = new java.util.PriorityQueue[Array[Int]]((a: Array[Int], b: Array[Int]) =>
        if (a(0) != b(0)) Integer.compare(a(0), b(0)) else Integer.compare(a(1), b(1))
      )
      i = 0
      while (i < n) { hh.offer(Array(nums(i), i)); i += 1 }
      var t = 0
      while (t < rem) {
        val cur = hh.poll()
        val v = ((cur(0).toLong * multiplier) % mod).toInt
        val idx = cur(1)
        nums(idx) = v
        hh.offer(Array(v, idx))
        t += 1
      }
      i = 0
      while (i < n) { nums(i) %= mod; i += 1 }
    } else {
      i = 0
      while (i < nums.length) { nums(i) %= mod; i += 1 }
    }
    nums
  }
}
