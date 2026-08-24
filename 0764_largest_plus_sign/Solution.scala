// LeetCode 0764 - Largest Plus Sign
// https://leetcode.com/problems/largest-plus-sign/

object Solution {
  def orderOfLargestPlusSign(n: Int, mines: Array[Array[Int]]): Int = {
    val banned = scala.collection.mutable.HashSet.empty[Int]
    for (mine <- mines) banned += mine(0) * n + mine(1)
    val arms = Array.ofDim[Int](n, n)
    var best = 0
    var r = 0
    while (r < n) {
      var count = 0
      var c = 0
      while (c < n) {
        count = if (banned.contains(r * n + c)) 0 else count + 1
        arms(r)(c) = count
        c += 1
      }
      count = 0
      c = n - 1
      while (c >= 0) {
        count = if (banned.contains(r * n + c)) 0 else count + 1
        arms(r)(c) = math.min(arms(r)(c), count)
        c -= 1
      }
      r += 1
    }
    var c = 0
    while (c < n) {
      var count = 0
      r = 0
      while (r < n) {
        count = if (banned.contains(r * n + c)) 0 else count + 1
        arms(r)(c) = math.min(arms(r)(c), count)
        r += 1
      }
      count = 0
      r = n - 1
      while (r >= 0) {
        count = if (banned.contains(r * n + c)) 0 else count + 1
        arms(r)(c) = math.min(arms(r)(c), count)
        best = math.max(best, arms(r)(c))
        r -= 1
      }
      c += 1
    }
    best
  }
}
