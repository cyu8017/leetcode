// LeetCode 3106 - Lexicographically Smallest String After Operations With Constraint
// https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/

object Solution {
  def getSmallestString(s: String, k0: Int): String = {
    var k = k0
    val arr = s.toCharArray
    var i = 0
    while (i < arr.length) {
      val c1 = arr(i)
      var c2 = 'a'
      var found = false
      while (c2 < c1 && !found) {
        val d = math.min(c1 - c2, 26 - (c1 - c2))
        if (d <= k) {
          arr(i) = c2
          k -= d
          found = true
        }
        c2 = (c2 + 1).toChar
      }
      i += 1
    }
    new String(arr)
  }
}
