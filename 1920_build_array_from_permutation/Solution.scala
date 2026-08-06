// LeetCode 1920 - Build Array from Permutation
// https://leetcode.com/problems/build-array-from-permutation/

object Solution {
  def buildArray(nums: Array[Int]): Array[Int] =
    nums.map(x => nums(x))
}
