// LeetCode 2952 - Minimum Number of Coins to be Added
// https://leetcode.com/problems/minimum-number-of-coins-to-be-added/

object Solution {
  def minimumAddedCoins(coins: Array[Int], target: Int): Int = {
    scala.util.Sorting.quickSort(coins)
    var ans = 0
    var reach = 0
    var i = 0
    while (reach < target) {
      if (i < coins.length && coins(i) <= reach + 1) {
        reach += coins(i)
        i += 1
      } else {
        reach += reach + 1
        ans += 1
      }
    }
    ans
  }
}
