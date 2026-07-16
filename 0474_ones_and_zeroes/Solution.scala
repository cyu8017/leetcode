// LeetCode 0474 - Ones and Zeroes
// https://leetcode.com/problems/ones-and-zeroes/

object Solution {
  def findMaxForm(strs: Array[String], m: Int, n: Int): Int = {
    val dp = Array.ofDim[Int](m + 1, n + 1)
    strs.foreach { string =>
      val zeros = string.count(_ == '0')
      val ones = string.count(_ == '1')
      var zero = m
      while (zero >= zeros) {
        var one = n
        while (one >= ones) {
          dp(zero)(one) = math.max(dp(zero)(one), dp(zero - zeros)(one - ones) + 1)
          one -= 1
        }
        zero -= 1
      }
    }
    dp(m)(n)
  }
}
