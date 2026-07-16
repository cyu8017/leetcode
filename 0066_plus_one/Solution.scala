// LeetCode 0066 - Plus One
// https://leetcode.com/problems/plus-one/

object Solution {
  def plusOne(digits: Array[Int]): Array[Int] = {
    val result = digits.clone

    var i = result.length - 1
    while (i >= 0) {
      if (result(i) < 9) {
        result(i) += 1
        return result
      }
      result(i) = 0
      i -= 1
    }

    Array(1) ++ result
  }
}
