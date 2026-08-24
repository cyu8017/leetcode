// LeetCode 0768 - Max Chunks To Make Sorted II
// https://leetcode.com/problems/max-chunks-to-make-sorted-ii/

object Solution {
  def maxChunksToSorted(arr: Array[Int]): Int = {
    val n = arr.length
    val maxLeft = Array.ofDim[Int](n)
    val minRight = Array.ofDim[Int](n)
    maxLeft(0) = arr(0)
    var i = 1
    while (i < n) {
      maxLeft(i) = math.max(maxLeft(i - 1), arr(i))
      i += 1
    }
    minRight(n - 1) = arr(n - 1)
    i = n - 2
    while (i >= 0) {
      minRight(i) = math.min(minRight(i + 1), arr(i))
      i -= 1
    }
    var chunks = 1
    i = 0
    while (i < n - 1) {
      if (maxLeft(i) <= minRight(i + 1)) chunks += 1
      i += 1
    }
    chunks
  }
}
