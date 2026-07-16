// LeetCode 0089 - Gray Code
// https://leetcode.com/problems/gray-code/

object Solution {
  def grayCode(n: Int): List[Int] = {
    val size = 1 << n
    (0 until size).map(i => i ^ (i >> 1)).toList
  }
}
