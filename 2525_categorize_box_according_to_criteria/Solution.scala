// LeetCode 2525 - Categorize Box According to Criteria
// https://leetcode.com/problems/categorize-box-according-to-criteria/

object Solution {
  def categorizeBox(length: Int, width: Int, height: Int, mass: Int): String = {
    val bulky = length >= 10000 || width >= 10000 || height >= 10000 ||
      length.toLong * width * height >= 1000000000L
    val heavy = mass >= 100
    if (bulky && heavy) "Both"
    else if (bulky) "Bulky"
    else if (heavy) "Heavy"
    else "Neither"
  }
}
