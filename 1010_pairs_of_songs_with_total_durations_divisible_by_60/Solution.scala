// LeetCode 1010 - Pairs of Songs With Total Durations Divisible by 60
// https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

object Solution {
  def numPairsDivisibleBy60(time: Array[Int]): Int = {
    val count = Array.fill(60)(0)
    var ans = 0
    for (t <- time) {
      ans += count((60 - t % 60) % 60)
      count(t % 60) += 1
    }
    ans
  }
}
