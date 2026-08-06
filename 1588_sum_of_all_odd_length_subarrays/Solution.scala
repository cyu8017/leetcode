// LeetCode 1588 - Sum of All Odd Length Subarrays
// https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

object Solution {
  def sumOddLengthSubarrays(arr: Array[Int]): Int = {
    val n = arr.length
    arr.zipWithIndex.map { case (x, i) => x * (((i + 1) * (n - i) + 1) / 2) }.sum
  }
}
