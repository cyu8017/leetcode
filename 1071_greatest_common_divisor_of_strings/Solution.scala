// LeetCode 1071 - Greatest Common Divisor of Strings
// https://leetcode.com/problems/greatest-common-divisor-of-strings/

object Solution {
  def gcdOfStrings(str1: String, str2: String): String = {
    if (str1 + str2 != str2 + str1) return ""
    def gcd(a: Int, b: Int): Int = if (b == 0) a else gcd(b, a % b)
    str1.substring(0, gcd(str1.length, str2.length))
  }
}
