// LeetCode 1985 - Find the Kth Largest Integer in the Array
// https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

object Solution {
  def kthLargestNumber(nums: Array[String], k: Int): String =
    nums.sortWith { (a, b) =>
      if (a.length != b.length) a.length > b.length else a > b
    }(k - 1)
}
