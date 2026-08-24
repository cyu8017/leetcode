// LeetCode 0769 - Max Chunks To Make Sorted
// https://leetcode.com/problems/max-chunks-to-make-sorted/

object Solution {
  def maxChunksToSorted(arr: Array[Int]): Int = {
    var chunks = 0
    var maxSoFar = 0
    var i = 0
    while (i < arr.length) {
      maxSoFar = math.max(maxSoFar, arr(i))
      if (maxSoFar == i) chunks += 1
      i += 1
    }
    chunks
  }
}
