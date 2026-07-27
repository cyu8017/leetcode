// LeetCode 1643 - Kth Smallest Instructions
// https://leetcode.com/problems/kth-smallest-instructions/

object Solution {
  def kthSmallestPath(destination: Array[Int], k: Int): String = {
    def comb(nn: Int, rr: Int): Long = {
      if (rr < 0 || rr > nn) return 0L
      var res = 1L
      val r = math.min(rr, nn - rr)
      var i = 0
      while (i < r) {
        res = res * (nn - i) / (i + 1)
        i += 1
      }
      res
    }
    var v = destination(0)
    var h = destination(1)
    var kk = k.toLong
    val ans = new StringBuilder
    while (h + v > 0) {
      if (h > 0) {
        val count = comb(h + v - 1, v)
        if (kk <= count) {
          ans.append('H')
          h -= 1
        } else {
          kk -= count
          ans.append('V')
          v -= 1
        }
      } else {
        ans.append('V')
        v -= 1
      }
    }
    ans.toString
  }
}
