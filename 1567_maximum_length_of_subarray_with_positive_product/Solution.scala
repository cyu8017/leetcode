// LeetCode 1567 - Maximum Length of Subarray With Positive Product
// https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

object Solution {
  def getMaxLen(nums: Array[Int]): Int = {
    var positive = 0
    var negative = 0
    var answer = 0
    for (x <- nums) {
      if (x == 0) { positive = 0; negative = 0 }
      else if (x > 0) {
        positive += 1
        negative = if (negative > 0) negative + 1 else 0
      } else {
        val np = if (negative > 0) negative + 1 else 0
        negative = positive + 1
        positive = np
      }
      answer = math.max(answer, positive)
    }
    answer
  }
}
