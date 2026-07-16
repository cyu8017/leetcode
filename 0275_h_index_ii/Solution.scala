// LeetCode 0275 - H-Index II
// https://leetcode.com/problems/h-index-ii/

object Solution {
  def hIndex(citations: Array[Int]): Int = {
    var left = 0
    var right = citations.length - 1
    val length = citations.length
    while (left <= right) {
      val mid = (left + right) / 2
      val papers = length - mid
      if (citations(mid) >= papers) right = mid - 1
      else left = mid + 1
    }
    length - left
  }
}
