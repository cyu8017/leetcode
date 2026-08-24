// LeetCode 2154 - Keep Multiplying Found Values by Two
// https://leetcode.com/problems/keep-multiplying-found-values-by-two/

object Solution {
  def findFinalValue(nums: Array[Int], original: Int): Int = {
    val have = nums.toSet
    var x = original
    while (have.contains(x)) x *= 2
    x
  }
}
