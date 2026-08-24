// LeetCode 2218 - Maximum Value of K Coins From Piles
// https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

object Solution {
  def maxValueOfCoins(piles: List[List[Int]], k: Int): Int = {
    var dp = Array.fill(k + 1)(0)
    for (pile <- piles) {
      val ndp = dp.clone()
      var sum = 0
      var take = 1
      while (take <= pile.size && take <= k) {
        sum += pile(take - 1)
        var j = take
        while (j <= k) {
          ndp(j) = math.max(ndp(j), dp(j - take) + sum)
          j += 1
        }
        take += 1
      }
      dp = ndp
    }
    dp(k)
  }
}
