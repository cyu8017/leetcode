// LeetCode 0078 - Subsets
// https://leetcode.com/problems/subsets/

object Solution {
  def subsets(nums: Array[Int]): List[List[Int]] = {
    val result = scala.collection.mutable.ListBuffer.empty[List[Int]]
    result += Nil

    for (num <- nums) {
      val size = result.length
      for (i <- 0 until size) {
        result += result(i) :+ num
      }
    }

    result.toList
  }
}
