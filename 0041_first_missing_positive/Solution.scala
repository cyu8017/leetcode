// LeetCode 0041 - First Missing Positive
// https://leetcode.com/problems/first-missing-positive/

object Solution {
  def firstMissingPositive(nums: Array[Int]): Int = {
    val n = nums.length
    var i = 0
    val arr = nums.clone

    while (i < n) {
      val value = arr(i)
      val target = value - 1
      if (value >= 1 && value <= n && arr(target) != value) {
        val temp = arr(i)
        arr(i) = arr(target)
        arr(target) = temp
      } else {
        i += 1
      }
    }

    var index = 0
    while (index < n) {
      if (arr(index) != index + 1) {
        return index + 1
      }
      index += 1
    }

    n + 1
  }
}
