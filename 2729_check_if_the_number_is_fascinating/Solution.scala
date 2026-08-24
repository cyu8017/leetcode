// LeetCode 2729 - Check if The Number is Fascinating
// https://leetcode.com/problems/check-if-the-number-is-fascinating/

object Solution {
  def isFascinating(n: Int): Boolean = {
    val s = n.toString + (2 * n).toString + (3 * n).toString
    if (s.length != 9) return false
    val cnt = Array.fill(10)(0)
    s.foreach(c => cnt(c - '0') += 1)
    if (cnt(0) != 0) return false
    var i = 1
    while (i <= 9) {
      if (cnt(i) != 1) return false
      i += 1
    }
    true
  }
}
