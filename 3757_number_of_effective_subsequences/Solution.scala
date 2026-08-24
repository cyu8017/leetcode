// LeetCode 3757 - Number of Effective Subsequences
// https://leetcode.com/problems/number-of-effective-subsequences/

object Solution {
  private def PopCount(x0: Int): Int = {
    var x = x0
    var c = 0
    while (x != 0) { c += x & 1; x >>= 1 }
    c
  }

  def countEffectiveSubsequences(nums: Array[Int]): Int = {
    val mod = 1000000007
    var all = 0
    nums.foreach(x => all |= x)
    val bits = new java.util.ArrayList[Integer]()
    var b = 0
    while (b < 20) {
      if (((all >> b) & 1) != 0) bits.add(b)
      b += 1
    }
    val m = bits.size()
    val freq = new Array[Int](1 << m)
    nums.foreach { x =>
      var mask = 0
      var i = 0
      while (i < m) {
        if (((x >> bits.get(i)) & 1) != 0) mask |= 1 << i
        i += 1
      }
      freq(mask) += 1
    }
    val disjoint = freq.clone()
    b = 0
    while (b < m) {
      var mask = 0
      while (mask < (1 << m)) {
        if (((mask >> b) & 1) != 0) disjoint(mask) += disjoint(mask ^ (1 << b))
        mask += 1
      }
      b += 1
    }
    val pow2 = new Array[Int](nums.length + 1)
    pow2(0) = 1
    var i = 1
    while (i <= nums.length) {
      pow2(i) = pow2(i - 1) * 2 % mod
      i += 1
    }
    var ans = 0
    val full = (1 << m) - 1
    var s = 1
    while (s <= full) {
      val ways = pow2(disjoint(full ^ s))
      val bc = PopCount(s)
      if ((bc & 1) != 0) {
        ans += ways
        if (ans >= mod) ans -= mod
      } else {
        ans -= ways
        if (ans < 0) ans += mod
      }
      s += 1
    }
    ans
  }
}
