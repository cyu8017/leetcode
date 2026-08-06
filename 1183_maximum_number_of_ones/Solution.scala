// LeetCode 1183 - Maximum Number of Ones
// https://leetcode.com/problems/maximum-number-of-ones/

object Solution {
  def maximumNumberOfOnes(width: Int, height: Int, sideLength: Int, maxOnes: Int): Int = {
    val counts = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (r <- 0 until sideLength; c <- 0 until sideLength) {
      val rows = (height - r + sideLength - 1) / sideLength
      val cols = (width - c + sideLength - 1) / sideLength
      counts += rows * cols
    }
    counts.sorted.reverse.take(maxOnes).sum
  }
}
