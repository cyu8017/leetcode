// LeetCode 3404 - Count Special Subsequences
// https://leetcode.com/problems/count-special-subsequences/

object Solution {
  def numberOfSubsequences(nums: Array[Int]): Long = {
    val n = nums.length
    var ans = 0L
    var i = 0
    while (i < n) {
      var j = i + 2
      while (j < n) {
        var k = j + 2
        while (k < n) {
          var l = k + 2
          while (l < n) {
            if (nums(i).toLong * nums(k) == nums(j).toLong * nums(l)) ans += 1
            l += 1
          }
          k += 1
        }
        j += 1
      }
      i += 1
    }
    ans
  }
}
