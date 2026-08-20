// LeetCode 1259 - Handshakes That Don't Cross
// https://leetcode.com/problems/handshakes-that-dont-cross/

object Solution {
  def numberOfWays(numPeople: Int): Int = {
    val mod = 1000000007
    val dp = Array.ofDim[Long](numPeople + 1)
    dp(0) = 1
    for (people <- 2 to numPeople by 2) {
      var sum = 0L
      for (left <- 0 until people by 2) {
        sum = (sum + dp(left) * dp(people - 2 - left)) % mod
      }
      dp(people) = sum
    }
    dp(numPeople).toInt
  }
}
