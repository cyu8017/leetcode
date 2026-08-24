// LeetCode 3827 - Count Monobit Integers
// https://leetcode.com/problems/count-monobit-integers/

object Solution {
  def countMonobit(n: Int): Int = {
    var ans = 1
    var i = 1
    var x = 1
    while (x <= n) {
      ans += 1
      x += (1 << i)
      i += 1
    }
    ans
  }
}
