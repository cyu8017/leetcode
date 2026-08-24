// LeetCode 0728 - Self Dividing Numbers
// https://leetcode.com/problems/self-dividing-numbers/

object Solution {
  def selfDividingNumbers(left: Int, right: Int): List[Int] = {
    def isSelfDividing(num: Int): Boolean = {
      var x = num
      while (x > 0) {
        val digit = x % 10
        if (digit == 0 || num % digit != 0) return false
        x /= 10
      }
      true
    }
    val result = scala.collection.mutable.ArrayBuffer.empty[Int]
    var num = left
    while (num <= right) {
      if (isSelfDividing(num)) result += num
      num += 1
    }
    result.toList
  }
}
