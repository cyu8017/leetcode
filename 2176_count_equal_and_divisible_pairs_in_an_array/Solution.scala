// LeetCode 2176 - Count Equal and Divisible Pairs in an Array
// https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

object Solution {
  def countPairs(nums: Array[Int], k: Int): Int = {
    var ans = 0
    var i = 0
    while (i < nums.length) {
      var j = i + 1
      while (j < nums.length) {
        if (nums(i) == nums(j) && (i * j) % k == 0) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
