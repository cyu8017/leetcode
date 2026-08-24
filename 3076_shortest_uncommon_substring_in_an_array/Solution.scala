// LeetCode 3076 - Shortest Uncommon Substring in an Array
// https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/

object Solution {
  def shortestSubstrings(arr: Array[String]): Array[String] = {
    val n = arr.length
    val ans = Array.fill(n)("")
    var i = 0
    while (i < n) {
      val s = arr(i)
      val m = s.length
      var j = 1
      while (j <= m && ans(i).isEmpty) {
        var l = 0
        while (l <= m - j) {
          val sub = s.substring(l, l + j)
          if (ans(i).isEmpty || ans(i).compareTo(sub) > 0) {
            var ok = true
            var k = 0
            while (k < n && ok) {
              if (k != i && arr(k).contains(sub)) ok = false
              k += 1
            }
            if (ok) ans(i) = sub
          }
          l += 1
        }
        j += 1
      }
      i += 1
    }
    ans
  }
}
