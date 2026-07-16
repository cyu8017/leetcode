// LeetCode 0507 - Perfect Number
// https://leetcode.com/problems/perfect-number/

object Solution {
  def checkPerfectNumber(num: Int): Boolean = {
    if (num <= 1) return false
    var total = 1
    val limit = math.sqrt(num).toInt
    for (divisor <- 2 to limit if num % divisor == 0) {
      total += divisor
      val pair = num / divisor
      if (pair != divisor) total += pair
    }
    total == num
  }
}
