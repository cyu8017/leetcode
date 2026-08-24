// LeetCode 3194 - Minimum Average of Smallest and Largest Elements
// https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/

object Solution {
  def minimumAverage(nums: Array[Int]): Double = {
    java.util.Arrays.sort(nums)
    val n = nums.length
    var ans = 1 << 30
    var i = 0
    while (i < n / 2) {
      ans = math.min(ans, nums(i) + nums(n - i - 1))
      i += 1
    }
    ans / 2.0
  }
}
