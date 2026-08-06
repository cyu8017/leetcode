// LeetCode 1566 - Detect Pattern of Length M Repeated K or More Times
// https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/

object Solution {
  def containsPattern(arr: Array[Int], m: Int, k: Int): Boolean = {
    var run = 0
    for (i <- m until arr.length) {
      run = if (arr(i) == arr(i - m)) run + 1 else 0
      if (run >= m * (k - 1)) return true
    }
    false
  }
}
