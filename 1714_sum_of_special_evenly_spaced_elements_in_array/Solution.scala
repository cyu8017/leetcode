// LeetCode 1714 - Sum Of Special Evenly-Spaced Elements In Array
// https://leetcode.com/problems/sum-of-special-evenly-spaced-elements-in-array/

object Solution {
  def solve(nums: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val mod = 1000000007L
    val n = nums.length
    val block = math.sqrt(n.toDouble).toInt + 1
    val dp = Array.ofDim[Int](block, n)
    for (step <- 1 until block) {
      for (i <- n - 1 to 0 by -1) {
        val next = if (i + step < n) dp(step)(i + step).toLong else 0L
        dp(step)(i) = ((nums(i) + next) % mod).toInt
      }
    }
    queries.map { query =>
      val start = query(0)
      val step = query(1)
      if (step < block) {
        dp(step)(start)
      } else {
        var total = 0L
        var i = start
        while (i < n) {
          total += nums(i)
          i += step
        }
        (total % mod).toInt
      }
    }
  }
}
