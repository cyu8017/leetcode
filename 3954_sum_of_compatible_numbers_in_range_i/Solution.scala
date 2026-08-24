// LeetCode 3954 - Sum of Compatible Numbers in Range I
// https://leetcode.com/problems/sum-of-compatible-numbers-in-range-i/

object Solution {
  def sumOfGoodIntegers(n: Int, k: Int): Int = {
    val start = math.max(1, n - k)
    val end = n + k
    var ans = 0
    var x = start
    while (x <= end) {
      if ((n & x) == 0) ans += x
      x += 1
    }
    ans
  }
}
