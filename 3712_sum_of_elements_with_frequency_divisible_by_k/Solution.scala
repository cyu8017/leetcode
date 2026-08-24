// LeetCode 3712 - Sum of Elements With Frequency Divisible by K
// https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/

object Solution {
  def sumDivisibleByK(nums: Array[Int], k: Int): Int = {
    val cnt = new java.util.HashMap[Integer, Integer]()
    for (x <- nums) cnt.merge(x, 1, Integer.sum)
    var ans = 0
    val it = cnt.entrySet().iterator()
    while (it.hasNext) {
      val e = it.next()
      if (e.getValue % k == 0) ans += e.getKey * e.getValue
    }
    ans
  }
}
