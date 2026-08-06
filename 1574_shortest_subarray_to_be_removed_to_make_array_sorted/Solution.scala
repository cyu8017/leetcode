// LeetCode 1574 - Shortest Subarray to be Removed to Make Array Sorted
// https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/

object Solution {
  def findLengthOfShortestSubarray(arr: Array[Int]): Int = {
    val n = arr.length
    var right = n - 1
    while (right > 0 && arr(right - 1) <= arr(right)) right -= 1
    if (right == 0) return 0
    var answer = right
    var left = 0
    while (left == 0 || (left < n && arr(left - 1) <= arr(left))) {
      while (right < n && arr(right) < arr(left)) right += 1
      answer = math.min(answer, right - left - 1)
      left += 1
      if (left >= n) return answer
    }
    answer
  }
}
