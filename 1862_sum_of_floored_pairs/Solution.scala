// LeetCode 1862 - Sum of Floored Pairs
// https://leetcode.com/problems/sum-of-floored-pairs/

object Solution {
  def sumOfFlooredPairs(nums: Array[Int]): Int = {
    val mod = 1000000007
    val maxVal = nums.max
    val count = Array.fill(maxVal + 1)(0)
    for (num <- nums) count(num) += 1

    val prefix = Array.fill(maxVal + 1)(0)
    prefix(0) = count(0)
    for (value <- 1 to maxVal) {
      prefix(value) = prefix(value - 1) + count(value)
    }

    var answer = 0L
    for (divisor <- 1 to maxVal if count(divisor) > 0) {
      var quotient = 1
      while (quotient.toLong * divisor <= maxVal) {
        val low = quotient * divisor
        val high = math.min((quotient + 1) * divisor - 1, maxVal)
        val matches = prefix(high) - (if (low > 0) prefix(low - 1) else 0)
        answer = (answer + count(divisor).toLong * matches * quotient) % mod
        quotient += 1
      }
    }
    answer.toInt
  }
}
