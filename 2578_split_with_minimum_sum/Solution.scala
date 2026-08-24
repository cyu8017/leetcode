// LeetCode 2578 - Split With Minimum Sum
// https://leetcode.com/problems/split-with-minimum-sum/

object Solution {
  def splitNum(num0: Int): Int = {
    var num = num0
    val digits = scala.collection.mutable.ArrayBuffer.empty[Int]
    while (num > 0) {
      digits += num % 10
      num /= 10
    }
    val sorted = digits.sorted
    var a = 0
    var b = 0
    var i = 0
    while (i < sorted.length) {
      if (i % 2 == 0) a = a * 10 + sorted(i)
      else b = b * 10 + sorted(i)
      i += 1
    }
    a + b
  }
}
