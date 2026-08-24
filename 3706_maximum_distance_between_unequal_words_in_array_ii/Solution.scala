// LeetCode 3706 - Maximum Distance Between Unequal Words in Array II
// https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-ii/

object Solution {
  def maxDistance(words: Array[String]): Int = {
    val n = words.length
    var ans = 0
    var i = 0
    while (i < n) {
      if (words(i) != words(0)) ans = math.max(ans, i + 1)
      if (words(i) != words(n - 1)) ans = math.max(ans, n - i)
      i += 1
    }
    ans
  }
}
