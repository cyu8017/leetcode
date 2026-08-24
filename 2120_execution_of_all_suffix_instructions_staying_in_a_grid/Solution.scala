// LeetCode 2120 - Execution of All Suffix Instructions Staying in a Grid
// https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/

object Solution {
  def executeInstructions(n: Int, startPos: Array[Int], s: String): Array[Int] = {
    val m = s.length
    val ans = Array.fill(m)(0)
    var i = 0
    while (i < m) {
      var r = startPos(0)
      var c = startPos(1)
      var cnt = 0
      var j = i
      var stop = false
      while (j < m && !stop) {
        val ch = s.charAt(j)
        if (ch == 'L') c -= 1
        else if (ch == 'R') c += 1
        else if (ch == 'U') r -= 1
        else r += 1
        if (r < 0 || r >= n || c < 0 || c >= n) stop = true
        else cnt += 1
        j += 1
      }
      ans(i) = cnt
      i += 1
    }
    ans
  }
}
