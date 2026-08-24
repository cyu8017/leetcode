// LeetCode 0763 - Partition Labels
// https://leetcode.com/problems/partition-labels/

object Solution {
  def partitionLabels(s: String): List[Int] = {
    val last = Array.fill(26)(0)
    var i = 0
    while (i < s.length) {
      last(s.charAt(i) - 'a') = i
      i += 1
    }
    var start = 0
    var end = 0
    val answer = scala.collection.mutable.ArrayBuffer.empty[Int]
    i = 0
    while (i < s.length) {
      end = math.max(end, last(s.charAt(i) - 'a'))
      if (i == end) {
        answer += end - start + 1
        start = i + 1
      }
      i += 1
    }
    answer.toList
  }
}
