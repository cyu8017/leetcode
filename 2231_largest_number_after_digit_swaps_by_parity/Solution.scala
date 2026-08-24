// LeetCode 2231 - Largest Number After Digit Swaps by Parity
// https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

object Solution {
  def largestInteger(num: Int): Int = {
    val digits = scala.collection.mutable.ArrayBuffer.empty[Int]
    var x = num
    while (x > 0) {
      digits.prepend(x % 10)
      x /= 10
    }
    val even = scala.collection.mutable.ArrayBuffer.empty[Int]
    val odd = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (d <- digits) {
      if (d % 2 == 0) even += d else odd += d
    }
    val ev = even.sorted(Ordering[Int].reverse)
    val od = odd.sorted(Ordering[Int].reverse)
    var ei = 0
    var oi = 0
    var ans = 0
    for (d <- digits) {
      if (d % 2 == 0) {
        ans = ans * 10 + ev(ei)
        ei += 1
      } else {
        ans = ans * 10 + od(oi)
        oi += 1
      }
    }
    ans
  }
}
