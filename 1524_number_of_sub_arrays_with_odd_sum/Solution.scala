// LeetCode 1524 - Number of Sub-arrays With Odd Sum
// https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

object Solution {
  def numOfSubarrays(arr: Array[Int]): Int = {
    val counts = Array(1, 0)
    var parity = 0
    var answer = 0L
    for (value <- arr) {
      parity ^= value & 1
      answer += counts(parity ^ 1)
      counts(parity) += 1
    }
    (answer % 1000000007L).toInt
  }
}
