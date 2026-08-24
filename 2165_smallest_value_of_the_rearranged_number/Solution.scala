// LeetCode 2165 - Smallest Value of the Rearranged Number
// https://leetcode.com/problems/smallest-value-of-the-rearranged-number/

object Solution {
  def smallestNumber(num: Long): Long = {
    var n = num
    val neg = n < 0
    if (neg) n = -n
    if (n == 0) return 0
    val digits = scala.collection.mutable.ArrayBuffer.empty[Char]
    while (n > 0) {
      digits += ('0' + (n % 10).toInt).toChar
      n /= 10
    }
    if (neg) {
      val sorted = digits.sorted(Ordering[Char].reverse)
      var ans = 0L
      sorted.foreach(d => ans = ans * 10 + (d - '0'))
      return -ans
    }
    val ds = digits.sorted
    if (ds(0) == '0') {
      var i = 1
      var swapped = false
      while (i < ds.length && !swapped) {
        if (ds(i) != '0') {
          val t = ds(0)
          ds(0) = ds(i)
          ds(i) = t
          swapped = true
        }
        i += 1
      }
    }
    var res = 0L
    ds.foreach(d => res = res * 10 + (d - '0'))
    res
  }
}
