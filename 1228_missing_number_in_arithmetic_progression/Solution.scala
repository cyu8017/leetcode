// LeetCode 1228 - Missing Number In Arithmetic Progression
// https://leetcode.com/problems/missing-number-in-arithmetic-progression/

object Solution {
  def missingNumber(arr: Array[Int]): Int = {
    val difference = (arr.last - arr.head) / arr.length
    for (i <- 1 until arr.length) {
      val expected = arr(0) + i * difference
      if (arr(i) != expected) return expected
    }
    arr(0)
  }
}
