// LeetCode 1317 - Convert Integer to the Sum of Two Zero-Free Integers
// https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

object Solution {
  def getNoZeroIntegers(n: Int): Array[Int] = {
    def valid(value: Int): Boolean = !value.toString.contains('0')
    for (first <- 1 until n) {
      if (valid(first) && valid(n - first)) return Array(first, n - first)
    }
    Array.empty[Int]
  }
}
