// LeetCode 0912 - Sort an Array
// https://leetcode.com/problems/sort-an-array/

object Solution {
  def sortArray(nums: Array[Int]): Array[Int] = {
    if (nums.length <= 1) return nums
    val mid = nums.length / 2
    val left = sortArray(nums.slice(0, mid))
    val right = sortArray(nums.slice(mid, nums.length))
    val merged = Array.ofDim[Int](nums.length)
    var i = 0
    var j = 0
    var k = 0
    while (i < left.length && j < right.length) {
      if (left(i) <= right(j)) { merged(k) = left(i); i += 1 }
      else { merged(k) = right(j); j += 1 }
      k += 1
    }
    while (i < left.length) { merged(k) = left(i); i += 1; k += 1 }
    while (j < right.length) { merged(k) = right(j); j += 1; k += 1 }
    merged
  }
}
