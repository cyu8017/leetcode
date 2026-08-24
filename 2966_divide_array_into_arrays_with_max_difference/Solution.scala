// LeetCode 2966 - Divide Array Into Arrays With Max Difference
// https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

object Solution {
  def divideArray(nums: Array[Int], k: Int): Array[Array[Int]] = {
    scala.util.Sorting.quickSort(nums)
    val ans = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    var i = 0
    while (i < nums.length) {
      if (nums(i + 2) - nums(i) > k) return Array.empty[Array[Int]]
      ans += Array(nums(i), nums(i + 1), nums(i + 2))
      i += 3
    }
    ans.toArray
  }
}
