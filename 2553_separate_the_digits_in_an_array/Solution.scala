// LeetCode 2553 - Separate the Digits in an Array
// https://leetcode.com/problems/separate-the-digits-in-an-array/

object Solution {
  def separateDigits(nums: Array[Int]): Array[Int] = {
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    nums.foreach { num =>
      var x = num
      val digits = scala.collection.mutable.ArrayBuffer.empty[Int]
      while (x > 0) {
        digits += x % 10
        x /= 10
      }
      var i = digits.size - 1
      while (i >= 0) {
        ans += digits(i)
        i -= 1
      }
    }
    ans.toArray
  }
}
