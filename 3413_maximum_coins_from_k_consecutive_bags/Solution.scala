// LeetCode 3413 - Maximum Coins From K Consecutive Bags
// https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/

object Solution {
  def maximumCoins(coins: Array[Array[Int]], k: Int): Long = {
    java.util.Arrays.sort(coins, (a: Array[Int], b: Array[Int]) => java.lang.Integer.compare(a(0), b(0)))
    var ans = 0L
    val n = coins.length
    var i = 0
    while (i < n) {
      var sum = 0L
      val start = coins(i)(0)
      val end = start + k - 1
      var j = i
      while (j < n && coins(j)(0) <= end) {
        var l = coins(j)(0)
        var r = coins(j)(1)
        if (r > end) r = end
        if (l < start) l = start
        if (l <= r) sum += (r - l + 1).toLong * coins(j)(2)
        j += 1
      }
      if (sum > ans) ans = sum
      i += 1
    }
    i = 0
    while (i < n) {
      var sum = 0L
      val end = coins(i)(1)
      val start = end - k + 1
      var j = 0
      while (j <= i) {
        var l = coins(j)(0)
        var r = coins(j)(1)
        if (l < start) l = start
        if (r > end) r = end
        if (l <= r) sum += (r - l + 1).toLong * coins(j)(2)
        j += 1
      }
      if (sum > ans) ans = sum
      i += 1
    }
    ans
  }
}
