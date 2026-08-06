// LeetCode 1561 - Maximum Number of Coins You Can Get
// https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

object Solution {
  def maxCoins(piles: Array[Int]): Int = {
    val sorted = piles.sorted
    sorted.slice(sorted.length / 3, sorted.length).zipWithIndex.collect { case (v, i) if i % 2 == 0 => v }.sum
  }
}
