// LeetCode 1291 - Sequential Digits
// https://leetcode.com/problems/sequential-digits/

object Solution {
  def sequentialDigits(low: Int, high: Int): List[Int] = {
    val digits = "123456789"
    val answer = scala.collection.mutable.ListBuffer.empty[Int]
    for (length <- 2 to 9; start <- 0 to 9 - length) {
      val value = digits.substring(start, start + length).toInt
      if (value >= low && value <= high) answer += value
    }
    answer.toList
  }
}
