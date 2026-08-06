// LeetCode 1569 - Number of Ways to Reorder Array to Get Same BST
// https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/

object Solution {
  def numOfWays(nums: Array[Int]): Int = {
    val MOD = 1000000007
    val n = nums.length
    val choose = Array.fill(n + 1, n + 1)(0)
    for (i <- 0 to n) {
      choose(i)(0) = 1
      choose(i)(i) = 1
      for (j <- 1 until i) choose(i)(j) = (choose(i - 1)(j - 1) + choose(i - 1)(j)) % MOD
    }
    def ways(values: List[Int]): Long = {
      if (values.length < 3) return 1L
      val left = values.tail.filter(_ < values.head)
      val right = values.tail.filter(_ > values.head)
      choose(values.length - 1)(left.length).toLong * ways(left) % MOD * ways(right) % MOD
    }
    ((ways(nums.toList) - 1 + MOD) % MOD).toInt
  }
}
