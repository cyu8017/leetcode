// LeetCode 2640 - Find the Score of All Prefixes of an Array
// https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/

object Solution {
  def findPrefixScore(nums: Array[Int]): Array[Long] = {
    val ans = new Array[Long](nums.length)
    var mx = 0
    var sum = 0L
    var i = 0
    while (i < nums.length) {
      if (nums(i) > mx) mx = nums(i)
      sum += nums(i) + mx
      ans(i) = sum
      i += 1
    }
    ans
  }
}
