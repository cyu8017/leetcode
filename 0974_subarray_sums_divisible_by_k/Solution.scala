// LeetCode 0974 - Subarray Sums Divisible by K
// https://leetcode.com/problems/subarray-sums-divisible-by-k/

object Solution {
  def subarraysDivByK(nums: Array[Int], k: Int): Int = {
    val count = scala.collection.mutable.Map(0 -> 1)
    var prefix = 0
    var ans = 0
    nums.foreach { x =>
      prefix = ((prefix + x) % k + k) % k
      ans += count.getOrElse(prefix, 0)
      count(prefix) = count.getOrElse(prefix, 0) + 1
    }
    ans
  }
}
