// LeetCode 2750 - Ways to Split Array Into Good Subarrays
// https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/

object Solution {
  def numberOfGoodSubarraySplits(nums: Array[Int]): Int = {
    val MOD = 1000000007
    val ones = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < nums.length) {
      if (nums(i) == 1) ones += i
      i += 1
    }
    if (ones.isEmpty) return 0
    var ans = 1L
    i = 1
    while (i < ones.length) {
      ans = ans * (ones(i) - ones(i - 1)) % MOD
      i += 1
    }
    ans.toInt
  }
}
