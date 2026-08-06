// LeetCode 1945 - Sum of Digits of String After Convert
// https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

object Solution {
  def getLucky(s: String, k: Int): Int = {
    var num = s.map(c => (c - 'a' + 1).toString).mkString
    for (_ <- 0 until k) {
      num = num.map(_ - '0').sum.toString
    }
    num.toInt
  }
}
