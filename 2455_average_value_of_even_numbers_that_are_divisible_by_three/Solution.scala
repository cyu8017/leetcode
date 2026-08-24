// LeetCode 2455 - Average Value of Even Numbers That Are Divisible by Three
// https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

object Solution {
  def averageValue(nums: Array[Int]): Int = {
    var sum = 0
    var cnt = 0
    var i = 0
    while (i < nums.length) {
      if (nums(i) % 6 == 0) {
        sum += nums(i)
        cnt += 1
      }
      i += 1
    }
    if (cnt == 0) 0 else sum / cnt
  }
}
