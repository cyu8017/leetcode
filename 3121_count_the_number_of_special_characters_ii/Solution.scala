// LeetCode 3121 - Count the Number of Special Characters II
// https://leetcode.com/problems/count-the-number-of-special-characters-ii/

object Solution {
  def numberOfSpecialChars(word: String): Int = {
    val first = new Array[Int](128)
    val last = new Array[Int](128)
    var i = 0
    while (i < word.length) {
      val c = word.charAt(i)
      if (first(c) == 0) first(c) = i + 1
      last(c) = i + 1
      i += 1
    }
    var ans = 0
    i = 0
    while (i < 26) {
      if (last('a' + i) > 0 && last('a' + i) < first('A' + i)) ans += 1
      i += 1
    }
    ans
  }
}
