// LeetCode 1542 - Find Longest Awesome Substring
// https://leetcode.com/problems/find-longest-awesome-substring/

object Solution {
  def longestAwesome(s: String): Int = {
    val first = scala.collection.mutable.Map(0 -> -1)
    var mask = 0
    var answer = 0
    for (i <- s.indices) {
      mask ^= 1 << (s(i) - '0')
      if (first.contains(mask)) answer = math.max(answer, i - first(mask))
      else first(mask) = i
      for (bit <- 0 until 10) {
        val candidate = mask ^ (1 << bit)
        if (first.contains(candidate)) answer = math.max(answer, i - first(candidate))
      }
    }
    answer
  }
}
