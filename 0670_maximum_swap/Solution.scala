// LeetCode 0670 - Maximum Swap
// https://leetcode.com/problems/maximum-swap/

object Solution {
  def maximumSwap(num: Int): Int = {
    val digits = num.toString.toCharArray
    val last = Array.fill(10)(-1)
    var i = 0
    while (i < digits.length) {
      last(digits(i) - '0') = i
      i += 1
    }
    i = 0
    while (i < digits.length) {
      var candidate = 9
      while (candidate > digits(i) - '0') {
        if (last(candidate) > i) {
          val tmp = digits(i)
          digits(i) = digits(last(candidate))
          digits(last(candidate)) = tmp
          return new String(digits).toInt
        }
        candidate -= 1
      }
      i += 1
    }
    num
  }
}
