// LeetCode 2575 - Find the Divisibility Array of a String
// https://leetcode.com/problems/find-the-divisibility-array-of-a-string/

object Solution {
  def divisibilityArray(word: String, m: Int): Array[Int] = {
    val ans = Array.fill(word.length)(0)
    var cur = 0L
    var i = 0
    while (i < word.length) {
      cur = (cur * 10 + (word.charAt(i) - '0')) % m
      if (cur == 0) ans(i) = 1
      i += 1
    }
    ans
  }
}
