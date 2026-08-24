// LeetCode 2740 - Find the Value of the Partition
// https://leetcode.com/problems/find-the-value-of-the-partition/

object Solution {
  def findValueOfPartition(nums: Array[Int]): Int = {
    val a = nums.sorted
    var ans = Int.MaxValue
    var i = 1
    while (i < a.length) {
      ans = math.min(ans, a(i) - a(i - 1))
      i += 1
    }
    ans
  }
}
