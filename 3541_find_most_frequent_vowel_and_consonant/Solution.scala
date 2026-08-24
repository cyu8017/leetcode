// LeetCode 3541 - Find Most Frequent Vowel and Consonant
// https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/

object Solution {
  def maxFreqSum(s: String): Int = {
    val cnt = new Array[Int](26)
    for (c <- s.toCharArray) cnt(c - 'a') += 1
    var a = 0
    var b = 0
    var i = 0
    while (i < 26) {
      val c = ('a' + i).toChar
      if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') a = math.max(a, cnt(i))
      else b = math.max(b, cnt(i))
      i += 1
    }
    a + b
  }
}
