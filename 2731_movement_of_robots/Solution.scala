// LeetCode 2731 - Movement of Robots
// https://leetcode.com/problems/movement-of-robots/

object Solution {
  def sumDistance(nums: Array[Int], s: String, d: Int): Int = {
    val MOD = 1000000007
    val n = nums.length
    val pos = Array.ofDim[Long](n)
    var i = 0
    while (i < n) {
      pos(i) = nums(i).toLong + (if (s.charAt(i) == 'R') d else -d)
      i += 1
    }
    java.util.Arrays.sort(pos)
    var ans = 0L
    var pref = 0L
    i = 0
    while (i < n) {
      ans = (ans + pos(i) * i - pref) % MOD
      pref += pos(i)
      i += 1
    }
    ((ans % MOD + MOD) % MOD).toInt
  }
}
