// LeetCode 3223 - Minimum Length of String After Operations
// https://leetcode.com/problems/minimum-length-of-string-after-operations/

object Solution {
  def minimumLength(s: String): Int = {
    val cnt = new Array[Int](26)
    var i = 0
    while (i < s.length) {
      cnt(s.charAt(i) - 'a') += 1
      i += 1
    }
    var ans = 0
    for (x <- cnt) if (x > 0) ans += (if ((x & 1) != 0) 1 else 2)
    ans
  }
}
