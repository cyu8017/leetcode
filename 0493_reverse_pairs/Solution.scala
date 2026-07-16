// LeetCode 0493 - Reverse Pairs
// https://leetcode.com/problems/reverse-pairs/

object Solution {
  def reversePairs(nums: Array[Int]): Int = mergeSort(nums, 0, nums.length - 1)

  private def mergeSort(nums: Array[Int], start: Int, end: Int): Int = {
    if (start >= end) return 0
    val mid = (start + end) / 2
    var count = mergeSort(nums, start, mid) + mergeSort(nums, mid + 1, end)
    var j = mid + 1
    for (i <- start to mid) {
      while (j <= end && nums(i) > 2L * nums(j)) j += 1
      count += j - (mid + 1)
    }
    val slice = nums.slice(start, end + 1).sorted
    for (index <- slice.indices) nums(start + index) = slice(index)
    count
  }
}
