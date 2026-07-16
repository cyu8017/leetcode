// LeetCode 0306 - Additive Number
// https://leetcode.com/problems/additive-number/

object Solution {
  def isAdditiveNumber(num: String): Boolean = {
    for (firstEnd <- 1 until num.length; secondEnd <- firstEnd + 1 until num.length) {
      if (valid(num, num.substring(0, firstEnd), num.substring(firstEnd, secondEnd), secondEnd)) {
        return true
      }
    }
    false
  }

  private def valid(num: String, first: String, second: String, start: Int): Boolean = {
    if ((first.length > 1 && first(0) == '0') || (second.length > 1 && second(0) == '0')) {
      return false
    }
    var currentStart = start
    var currentFirst = first
    var currentSecond = second
    while (currentStart < num.length) {
      val total = addStrings(currentFirst, currentSecond)
      if (!num.startsWith(total, currentStart)) {
        return false
      }
      currentFirst = currentSecond
      currentSecond = total
      currentStart += total.length
    }
    true
  }

  private def addStrings(left: String, right: String): String = {
    (BigInt(left) + BigInt(right)).toString
  }
}
