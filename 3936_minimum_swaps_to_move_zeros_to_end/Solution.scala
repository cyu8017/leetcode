// LeetCode 3936 - Minimum Swaps to Move Zeros to End
// https://leetcode.com/problems/minimum-swaps-to-move-zeros-to-end/

object Solution {
  def minimumSwaps(nums: Array[Int]): Int = {
    var ans = 0
    val n = nums.length
    var i = 0
    var j = n - 1
    while (i < j) {
      while (i < n && nums(i) != 0) i += 1
      while (j > 0 && nums(j) == 0) j -= 1
      if (i >= j) i = j
      else {
        ans += 1
        i += 1
        j -= 1
      }
    }
    ans
  }
}
