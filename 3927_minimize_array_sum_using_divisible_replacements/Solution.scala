// LeetCode 3927 - Minimize Array Sum Using Divisible Replacements
// https://leetcode.com/problems/minimize-array-sum-using-divisible-replacements/

object Solution {
  def minArraySum(nums: Array[Int]): Long = {
    var maximum = 0
    val present = new Array[Boolean](100001)
    for (value <- nums) {
      present(value) = true
      if (value > maximum) maximum = value
    }
    val best = new Array[Int](maximum + 1)
    var divisor = 1
    while (divisor <= maximum) {
      if (present(divisor)) {
        var multiple = divisor
        while (multiple <= maximum) {
          if (best(multiple) == 0) best(multiple) = divisor
          multiple += divisor
        }
      }
      divisor += 1
    }
    var answer = 0L
    for (value <- nums) answer += best(value)
    answer
  }
}
