// LeetCode 3442 - Maximum Difference Between Even and Odd Frequency I
// https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/

object Solution {
  def maxDifference(s: String): Int = {
    val freq = new Array[Int](26)
    s.foreach { c => freq(c - 'a') += 1 }
    var maxOdd = 0
    var minEven = 1000000000
    freq.foreach { f =>
      if (f != 0) {
        if (f % 2 == 1) {
          if (f > maxOdd) maxOdd = f
        } else if (f < minEven) minEven = f
      }
    }
    maxOdd - minEven
  }
}
