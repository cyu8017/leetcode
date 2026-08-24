// LeetCode 3952 - Maximum Total Value of Covered Indices
// https://leetcode.com/problems/maximum-total-value-of-covered-indices/

object Solution {
  def maxTotalValue(nums: Array[Int], s: String): Int = {
    var answer = 0
    var i = 0
    while (i < s.length) {
      if (s.charAt(i) == '0') i += 1
      else {
        val start = i
        while (i < s.length && s.charAt(i) == '1') i += 1
        val end = i - 1
        if (start == 0) {
          var index = start
          while (index <= end) {
            answer += nums(index)
            index += 1
          }
        } else {
          var minimum = nums(start - 1)
          var total = 0
          var index = start - 1
          while (index <= end) {
            total += nums(index)
            if (nums(index) < minimum) minimum = nums(index)
            index += 1
          }
          answer += total - minimum
        }
      }
    }
    answer
  }
}
