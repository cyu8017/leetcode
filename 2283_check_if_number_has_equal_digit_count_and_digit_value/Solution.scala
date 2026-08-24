// LeetCode 2283 - Check if Number Has Equal Digit Count and Digit Value
// https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

object Solution {
  def digitCount(num: String): Boolean = {
    val cnt = new Array[Int](10)
    var i = 0
    while (i < num.length) {
      cnt(num.charAt(i) - '0') += 1
      i += 1
    }
    i = 0
    while (i < num.length) {
      if (cnt(i) != num.charAt(i) - '0') return false
      i += 1
    }
    true
  }
}
