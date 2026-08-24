// LeetCode 3432 - Count Partitions with Even Sum Difference
// https://leetcode.com/problems/count-partitions-with-even-sum-difference/

object Solution {
  def countPartitions(nums: Array[Int]): Int = {
    var total = 0
    nums.foreach(x => total += x)
    var ans = 0
    var left = 0
    var i = 0
    while (i < nums.length - 1) {
      left += nums(i)
      if ((left - (total - left)) % 2 == 0) ans += 1
      i += 1
    }
    ans
  }
}
