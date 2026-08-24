// LeetCode 0744 - Find Smallest Letter Greater Than Target
// https://leetcode.com/problems/find-smallest-letter-greater-than-target/

object Solution {
  def nextGreatestLetter(letters: Array[Char], target: Char): Char = {
    var left = 0
    var right = letters.length
    while (left < right) {
      val mid = left + (right - left) / 2
      if (letters(mid) <= target) left = mid + 1
      else right = mid
    }
    letters(left % letters.length)
  }
}
