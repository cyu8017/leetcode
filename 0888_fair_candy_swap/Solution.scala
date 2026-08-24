// LeetCode 0888 - Fair Candy Swap
// https://leetcode.com/problems/fair-candy-swap/

object Solution {
  def fairCandySwap(aliceSizes: Array[Int], bobSizes: Array[Int]): Array[Int] = {
    val sumA = aliceSizes.sum
    val sumB = bobSizes.sum
    val diff = (sumA - sumB) / 2
    val bob = bobSizes.toSet
    aliceSizes.foreach { a =>
      if (bob.contains(a - diff)) return Array(a, a - diff)
    }
    Array.empty[Int]
  }
}
