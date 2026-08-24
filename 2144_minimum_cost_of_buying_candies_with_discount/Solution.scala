// LeetCode 2144 - Minimum Cost of Buying Candies With Discount
// https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

object Solution {
  def minimumCost(cost: Array[Int]): Int = {
    val arr = cost.sorted(Ordering[Int].reverse)
    var ans = 0
    var i = 0
    while (i < arr.length) {
      if (i % 3 != 2) ans += arr(i)
      i += 1
    }
    ans
  }
}
