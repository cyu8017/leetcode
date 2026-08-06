// LeetCode 1520 - Maximum Number of Non-Overlapping Substrings
// https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/

object Solution {
  def maxNumOfSubstrings(s: String): List[String] = {
    val first = Array.fill(26)(-1)
    val last = Array.fill(26)(-1)
    for (i <- s.indices) {
      val c = s(i) - 'a'
      if (first(c) < 0) first(c) = i
      last(c) = i
    }
    val intervals = scala.collection.mutable.ArrayBuffer.empty[(Int, Int)]
    for (i <- s.indices if first(s(i) - 'a') == i) {
      var end = last(s(i) - 'a')
      var j = i
      var valid = true
      while (j <= end && valid) {
        if (first(s(j) - 'a') < i) valid = false
        else {
          end = math.max(end, last(s(j) - 'a'))
          j += 1
        }
      }
      if (valid) intervals += ((end, i))
    }
    val sorted = intervals.sortBy(_._1)
    val answer = scala.collection.mutable.ArrayBuffer.empty[String]
    var previousEnd = -1
    for ((end, start) <- sorted if start > previousEnd) {
      answer += s.substring(start, end + 1)
      previousEnd = end
    }
    answer.sortBy(_.length).toList
  }
}
