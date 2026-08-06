// LeetCode 1968 - Array With Elements Not Equal to Average of Neighbors
// https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

object Solution {
  def rearrangeArray(nums: Array[Int]): Array[Int] = {
    val sorted = nums.sorted
    val n = sorted.length
    val mid = (n + 1) / 2
    val small = sorted.take(mid)
    val large = sorted.drop(mid)
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    var j = 0
    while (i < small.length || j < large.length) {
      if (i < small.length) { ans += small(i); i += 1 }
      if (j < large.length) { ans += large(j); j += 1 }
    }
    ans.toArray
  }
}
