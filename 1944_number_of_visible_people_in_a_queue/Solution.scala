// LeetCode 1944 - Number of Visible People in a Queue
// https://leetcode.com/problems/number-of-visible-people-in-a-queue/

object Solution {
  def canSeePersonsCount(heights: Array[Int]): Array[Int] = {
    val n = heights.length
    val ans = Array.ofDim[Int](n)
    val stack = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (i <- n - 1 to 0 by -1) {
      var count = 0
      while (stack.nonEmpty && heights(i) > stack.last) {
        stack.remove(stack.length - 1)
        count += 1
      }
      if (stack.nonEmpty) count += 1
      ans(i) = count
      stack += heights(i)
    }
    ans
  }
}
