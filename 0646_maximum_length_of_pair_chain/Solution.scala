// LeetCode 0646 - Maximum Length of Pair Chain
// https://leetcode.com/problems/maximum-length-of-pair-chain/

object Solution {
  def findLongestChain(pairs: Array[Array[Int]]): Int = {
    val sorted = pairs.sortBy(_(1))
    var length = 0
    var currentEnd = Int.MinValue
    sorted.foreach { pair =>
      if (pair(0) > currentEnd) {
        length += 1
        currentEnd = pair(1)
      }
    }
    length
  }
}
