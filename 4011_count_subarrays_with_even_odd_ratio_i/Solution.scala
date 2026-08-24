// LeetCode 4011 - Count Subarrays With Even Odd Ratio I
// https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-i/

object Solution {
  def countRatioSubarrays(nums: Array[Int], a: Int, b: Int): Int = {
    val n = nums.length
    var ans = 0L
    var i = 0
    while (i < n) {
      var y = 0
      var j = i
      while (j < n) {
        y += nums(j) % 2
        val x = j - i + 1 - y
        if (y > 0 && x.toLong * b <= y.toLong * a) ans += 1
        j += 1
      }
      i += 1
    }
    ans.toInt
  }
}
