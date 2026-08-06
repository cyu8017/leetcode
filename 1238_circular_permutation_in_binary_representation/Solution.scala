// LeetCode 1238 - Circular Permutation in Binary Representation
// https://leetcode.com/problems/circular-permutation-in-binary-representation/

object Solution {
  def circularPermutation(n: Int, start: Int): List[Int] =
    (0 until (1 << n)).map(i => start ^ i ^ (i >> 1)).toList
}
