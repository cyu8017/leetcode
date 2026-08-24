// LeetCode 0645 - Set Mismatch
// https://leetcode.com/problems/set-mismatch/

object Solution {
  def findErrorNums(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val seen = Array.fill(n + 1)(0)
    nums.foreach(value => seen(value) += 1)
    var duplicate = -1
    var missing = -1
    var value = 1
    while (value <= n) {
      if (seen(value) == 2) duplicate = value
      else if (seen(value) == 0) missing = value
      value += 1
    }
    Array(duplicate, missing)
  }
}
