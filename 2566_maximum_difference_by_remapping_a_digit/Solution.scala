// LeetCode 2566 - Maximum Difference by Remapping a Digit
// https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

object Solution {
  def minMaxDifference(num: Int): Int = {
    val s = num.toString
    var maxV = num
    s.foreach { c =>
      if (c != '9') {
        maxV = remap(s, c, '9')
        return maxV - remap(s, s.charAt(0), '0')
      }
    }
    maxV - remap(s, s.charAt(0), '0')
  }

  private def remap(s: String, from: Char, to: Char): Int = {
    var v = 0
    s.foreach { c =>
      val d = if (c == from) to else c
      v = v * 10 + (d - '0')
    }
    v
  }
}
