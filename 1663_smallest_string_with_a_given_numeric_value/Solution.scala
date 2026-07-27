// LeetCode 1663 - Smallest String With A Given Numeric Value
// https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

object Solution {
  def getSmallestString(n: Int, k: Int): String = {
    val a = Array.fill(n)('a')
    var rem = k - n
    var i = n - 1
    while (i >= 0 && rem > 0) {
      val d = math.min(25, rem)
      a(i) = ('a' + d).toChar
      rem -= d
      i -= 1
    }
    a.mkString
  }
}
