// LeetCode 0438 - Find All Anagrams in a String
// https://leetcode.com/problems/find-all-anagrams-in-a-string/

import scala.collection.mutable

object Solution {
  def findAnagrams(s: String, p: String): List[Int] = {
    if (p.length > s.length) {
      return List.empty
    }

    val need = Array.fill(26)(0)
    val window = Array.fill(26)(0)
    for (char <- p) {
      need(char - 'a') += 1
    }

    val result = mutable.ListBuffer.empty[Int]
    var left = 0
    for (right <- s.indices) {
      window(s(right) - 'a') += 1
      if (right - left + 1 > p.length) {
        window(s(left) - 'a') -= 1
        left += 1
      }
      if (window.sameElements(need)) {
        result += left
      }
    }
    result.toList
  }
}
