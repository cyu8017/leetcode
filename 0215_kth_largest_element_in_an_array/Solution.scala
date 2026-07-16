// LeetCode 0215 - Kth Largest Element in an Array
// https://leetcode.com/problems/kth-largest-element-in-an-array/

import scala.util.Random

object Solution {
  private val random = new Random()

  def findKthLargest(nums: Array[Int], k: Int): Int = {
    val target = nums.length - k
    var left = 0
    var right = nums.length - 1
    while (left <= right) {
      val pivotIndex = partition(nums, left, right)
      if (pivotIndex == target) return nums(pivotIndex)
      if (pivotIndex < target) left = pivotIndex + 1 else right = pivotIndex - 1
    }
    nums(left)
  }

  private def partition(nums: Array[Int], left: Int, right: Int): Int = {
    val pivotIndex = left + random.nextInt(right - left + 1)
    swap(nums, pivotIndex, right)
    var store = left
    for (i <- left until right) {
      if (nums(i) <= nums(right)) {
        swap(nums, store, i)
        store += 1
      }
    }
    swap(nums, store, right)
    store
  }

  private def swap(nums: Array[Int], i: Int, j: Int): Unit = {
    val temp = nums(i)
    nums(i) = nums(j)
    nums(j) = temp
  }
}
