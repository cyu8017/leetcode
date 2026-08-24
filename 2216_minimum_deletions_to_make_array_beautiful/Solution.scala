// LeetCode 2216 - Minimum Deletions to Make Array Beautiful
// https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/

object Solution {
  def minDeletion(nums: Array[Int]): Int = {
    var ans = 0
    var i = 0
    val n = nums.length
    while (i + 1 < n) {
      if (nums(i) == nums(i + 1)) {
        ans += 1
        i += 1
      } else i += 2
    }
    if ((n - ans) % 2 != 0) ans += 1
    ans
  }
}
