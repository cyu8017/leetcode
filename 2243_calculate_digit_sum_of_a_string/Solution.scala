// LeetCode 2243 - Calculate Digit Sum of a String
// https://leetcode.com/problems/calculate-digit-sum-of-a-string/

object Solution {
  def digitSum(s0: String, k: Int): String = {
    var s = s0
    while (s.length > k) {
      val next = new StringBuilder
      var i = 0
      while (i < s.length) {
        var sum = 0
        val end = math.min(i + k, s.length)
        var j = i
        while (j < end) {
          sum += s.charAt(j) - '0'
          j += 1
        }
        next.append(sum)
        i += k
      }
      s = next.toString
    }
    s
  }
}
