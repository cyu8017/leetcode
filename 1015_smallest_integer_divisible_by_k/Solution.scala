// LeetCode 1015 - Smallest Integer Divisible by K
// https://leetcode.com/problems/smallest-integer-divisible-by-k/

object Solution {
  def smallestRepunitDivByK(k: Int): Int = {
    if (k % 2 == 0 || k % 5 == 0) return -1
    var rem = 0
    for (length <- 1 to k) {
      rem = (rem * 10 + 1) % k
      if (rem == 0) return length
    }
    -1
  }
}
