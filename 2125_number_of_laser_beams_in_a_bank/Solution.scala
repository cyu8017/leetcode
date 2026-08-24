// LeetCode 2125 - Number of Laser Beams in a Bank
// https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

object Solution {
  def numberOfBeams(bank: Array[String]): Int = {
    var ans = 0
    var prev = 0
    bank.foreach { row =>
      var cnt = 0
      var i = 0
      while (i < row.length) {
        if (row.charAt(i) == '1') cnt += 1
        i += 1
      }
      if (cnt > 0) {
        ans += prev * cnt
        prev = cnt
      }
    }
    ans
  }
}
