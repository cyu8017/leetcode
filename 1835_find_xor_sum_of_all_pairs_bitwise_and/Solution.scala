// LeetCode 1835 - Find XOR Sum of All Pairs Bitwise AND
// https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/

object Solution {
  def getXORSum(arr1: Array[Int], arr2: Array[Int]): Int =
    arr1.foldLeft(0)(_ ^ _) & arr2.foldLeft(0)(_ ^ _)
}
