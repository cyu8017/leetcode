// LeetCode 1331 - Rank Transform of an Array
// https://leetcode.com/problems/rank-transform-of-an-array/

object Solution {
  def arrayRankTransform(arr: Array[Int]): Array[Int] = {
    val sorted = arr.distinct.sorted
    val rank = sorted.zipWithIndex.map { case (v, i) => v -> (i + 1) }.toMap
    arr.map(rank)
  }
}
