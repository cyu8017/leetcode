// LeetCode 0477 - Total Hamming Distance
// https://leetcode.com/problems/total-hamming-distance/

object Solution {
  def totalHammingDistance(nums: Array[Int]): Int = {
    var total = 0
    var bit = 0
    while (bit < 32) {
      var zeros = 0
      var ones = 0
      nums.foreach { value =>
        if ((value & (1 << bit)) != 0) ones += 1 else zeros += 1
      }
      total += zeros * ones
      bit += 1
    }
    total
  }
}
