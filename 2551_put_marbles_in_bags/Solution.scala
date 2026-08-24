// LeetCode 2551 - Put Marbles in Bags
// https://leetcode.com/problems/put-marbles-in-bags/

object Solution {
  def putMarbles(weights: Array[Int], k: Int): Long = {
    val n = weights.length
    if (k == 1 || k == n) return 0
    val pair = Array.fill(n - 1)(0)
    var i = 0
    while (i < n - 1) {
      pair(i) = weights(i) + weights(i + 1)
      i += 1
    }
    java.util.Arrays.sort(pair)
    var mn = 0L
    var mx = 0L
    i = 0
    while (i < k - 1) {
      mn += pair(i)
      mx += pair(n - 2 - i)
      i += 1
    }
    mx - mn
  }
}
