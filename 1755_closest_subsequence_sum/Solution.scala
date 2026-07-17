// LeetCode 1755 - Closest Subsequence Sum
// https://leetcode.com/problems/closest-subsequence-sum/

object Solution {
  def minAbsDifference(nums: Array[Int], goal: Int): Int = {
    val n = nums.length
    val left = nums.slice(0, n / 2)
    val right = nums.slice(n / 2, n)

    def sums(arr: Array[Int]): Array[Long] = {
      val vals = new Array[Long](1 << arr.length)
      var size = 1
      for (x <- arr) {
        var i = 0
        while (i < size) {
          vals(size + i) = vals(i) + x
          i += 1
        }
        size *= 2
      }
      java.util.Arrays.sort(vals)
      vals
    }

    val a = sums(left)
    val b = sums(right)
    var best = Long.MaxValue
    var j = b.length - 1
    for (x <- a) {
      while (j > 0 && math.abs(x + b(j) - goal) >= math.abs(x + b(j - 1) - goal)) {
        j -= 1
      }
      best = math.min(best, math.abs(x + b(j) - goal))
    }
    best.toInt
  }
}
