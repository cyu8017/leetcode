// LeetCode 1893 - Check if All the Integers in a Range Are Covered
// https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

object Solution {
  def isCovered(ranges: Array[Array[Int]], left: Int, right: Int): Boolean = {
    val covered = Array.fill(51)(false)
    for (r <- ranges; value <- r(0) to r(1)) {
      covered(value) = true
    }
    (left to right).forall(covered)
  }
}
