// LeetCode 3557 - Find Maximum Number of Non Intersecting Substrings
// https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/

object Solution {
  def maxSubstrings(word: String): Int = {
    var ans = 0
    val first = scala.collection.mutable.HashMap.empty[Char, Int]
    var i = 0
    while (i < word.length) {
      val c = word.charAt(i)
      if (!first.contains(c)) first(c) = i
      else if (i - first(c) + 1 >= 4) {
        ans += 1
        first.clear()
      }
      i += 1
    }
    ans
  }
}
