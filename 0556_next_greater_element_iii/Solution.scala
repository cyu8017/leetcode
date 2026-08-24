// LeetCode 0556 - Next Greater Element III
// https://leetcode.com/problems/next-greater-element-iii/

object Solution {
  def nextGreaterElement(n: Int): Int = {
    val digits = n.toString.toCharArray
    var i = digits.length - 2
    while (i >= 0 && digits(i) >= digits(i + 1)) i -= 1
    if (i < 0) return -1
    var j = digits.length - 1
    while (digits(j) <= digits(i)) j -= 1
    val tmp = digits(i)
    digits(i) = digits(j)
    digits(j) = tmp
    reverse(digits, i + 1, digits.length - 1)
    var value = 0L
    digits.foreach(ch => value = value * 10 + (ch - '0'))
    if (value > Int.MaxValue) -1 else value.toInt
  }

  private def reverse(digits: Array[Char], left0: Int, right0: Int): Unit = {
    var left = left0
    var right = right0
    while (left < right) {
      val tmp = digits(left)
      digits(left) = digits(right)
      digits(right) = tmp
      left += 1
      right -= 1
    }
  }
}
