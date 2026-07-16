// LeetCode 0274 - H-Index
// https://leetcode.com/problems/h-index/

object Solution {
  def hIndex(citations: Array[Int]): Int = {
    val buckets = Array.fill(citations.length + 1)(0)
    for (citation <- citations) {
      buckets(math.min(citation, citations.length)) += 1
    }
    var total = 0
    var h = buckets.length - 1
    while (h >= 0) {
      total += buckets(h)
      if (total >= h) return h
      h -= 1
    }
    0
  }
}
