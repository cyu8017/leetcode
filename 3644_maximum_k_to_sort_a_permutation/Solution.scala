// LeetCode 3644 - Maximum K to Sort a Permutation
// https://leetcode.com/problems/maximum-k-to-sort-a-permutation/

object Solution {
  def sortPermutation(nums: Array[Int]): Int = {
    var ans = -1
    var i = 0
    while (i < nums.length) {
      if (i != nums(i)) ans &= nums(i)
      i += 1
    }
    math.max(ans, 0)
  }
}
