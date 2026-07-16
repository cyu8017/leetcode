// LeetCode 0479 - Largest Palindrome Product
// https://leetcode.com/problems/largest-palindrome-product/

object Solution {
  def largestPalindrome(n: Int): Int = {
    if (n == 1) return 9
    val upper = math.pow(10, n).toInt - 1
    val lower = math.pow(10, n - 1).toInt
    var first = upper
    while (first >= lower) {
      val candidate = (first.toString + first.toString.reverse).toLong
      var factor = upper
      while (factor.toLong * factor >= candidate) {
        if (candidate % factor == 0) {
          val partner = candidate / factor
          if (partner >= lower && partner <= upper) {
            return (candidate % 1337).toInt
          }
        }
        factor -= 1
      }
      first -= 1
    }
    0
  }
}
