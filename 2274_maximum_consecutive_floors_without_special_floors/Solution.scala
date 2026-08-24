// LeetCode 2274 - Maximum Consecutive Floors Without Special Floors
// https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/

object Solution {
  def maxConsecutive(bottom: Int, top: Int, special: Array[Int]): Int = {
    java.util.Arrays.sort(special)
    var ans = special(0) - bottom
    var i = 1
    while (i < special.length) {
      ans = math.max(ans, special(i) - special(i - 1) - 1)
      i += 1
    }
    math.max(ans, top - special(special.length - 1))
  }
}
