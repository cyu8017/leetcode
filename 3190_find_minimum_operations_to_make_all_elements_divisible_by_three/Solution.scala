// LeetCode 3190 - Find Minimum Operations to Make All Elements Divisible by Three
// https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

object Solution {
  def minimumOperations(nums: Array[Int]): Int = {
    var ans = 0
    for (x <- nums) if (x % 3 != 0) ans += 1
    ans
  }
}
