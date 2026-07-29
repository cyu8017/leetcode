// LeetCode 1018 - Binary Prefix Divisible By 5
// https://leetcode.com/problems/binary-prefix-divisible-by-5/

object Solution {
  def prefixesDivBy5(nums: Array[Int]): Array[Boolean] = {
    val ans = Array.ofDim[Boolean](nums.length)
    var rem = 0
    for (i <- nums.indices) {
      rem = (rem * 2 + nums(i)) % 5
      ans(i) = rem == 0
    }
    ans
  }
}
