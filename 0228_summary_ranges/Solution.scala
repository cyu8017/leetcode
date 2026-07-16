// LeetCode 0228 - Summary Ranges
// https://leetcode.com/problems/summary-ranges/

import scala.collection.mutable

object Solution {
  def summaryRanges(nums: Array[Int]): Array[String] = {
    val result = mutable.ArrayBuffer.empty[String]
    var index = 0

    while (index < nums.length) {
      val start = nums(index)
      while (index + 1 < nums.length && nums(index + 1) == nums(index) + 1) {
        index += 1
      }
      if (start == nums(index)) {
        result += start.toString
      } else {
        result += s"$start->${nums(index)}"
      }
      index += 1
    }

    result.toArray
  }
}
