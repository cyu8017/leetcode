// LeetCode 3806 - Maximum Bitwise And After Increment Operations
// https://leetcode.com/problems/maximum-bitwise-and-after-increment-operations/

object Solution {
  private def BitLen(x0: Int): Int = {
    var x = x0
    if (x == 0) return 0
    var n = 0
    while (x > 0) { n += 1; x >>= 1 }
    n
  }

  def maximumAND(nums: Array[Int], k: Int, m: Int): Int = {
    var mxVal = nums(0)
    nums.foreach(v => if (v > mxVal) mxVal = v)
    mxVal += k
    val mx = BitLen(mxVal)
    var ans = 0
    val cost = new Array[Int](nums.length)
    var bit = mx - 1
    while (bit >= 0) {
      val target = ans | (1 << bit)
      var i = 0
      while (i < nums.length) {
        val x = nums(i)
        val j = BitLen(target & ~x)
        val mask = (1 << j) - 1
        cost(i) = (target & mask) - (x & mask)
        i += 1
      }
      java.util.Arrays.sort(cost)
      var sum = 0
      i = 0
      while (i < m) {
        sum += cost(i)
        i += 1
      }
      if (sum <= k) ans = target
      bit -= 1
    }
    ans
  }
}
