// LeetCode 3254 - Find the Power of K-Size Subarrays I
// https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/

object Solution {
  def resultsArray(nums: Array[Int], k: Int): Array[Int] = {
    val n = nums.length
    val ans = new Array[Int](n - k + 1)
    var i = 0
    while (i <= n - k) {
      var ok = true
      var j = i + 1
      while (j < i + k) {
        if (nums(j) != nums(j - 1) + 1) { ok = false; j = i + k }
        else j += 1
      }
      ans(i) = if (ok) nums(i + k - 1) else -1
      i += 1
    }
    ans
  }
}
