// LeetCode 3216 - Lexicographically Smallest String After a Swap
// https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/

object Solution {
  def getSmallestString(s: String): String = {
    val arr = s.toCharArray
    val n = arr.length
    var i = 1
    while (i < n) {
      val a = arr(i - 1)
      val b = arr(i)
      if (a > b && (a % 2) == (b % 2)) {
        arr(i - 1) = b
        arr(i) = a
        return new String(arr)
      }
      i += 1
    }
    s
  }
}
