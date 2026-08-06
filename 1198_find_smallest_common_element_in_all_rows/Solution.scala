// LeetCode 1198 - Find Smallest Common Element in All Rows
// https://leetcode.com/problems/find-smallest-common-element-in-all-rows/

object Solution {
  def smallestCommonElement(mat: Array[Array[Int]]): Int = {
    var common = mat(0).toSet
    for (row <- mat.tail) {
      common = common.intersect(row.toSet)
      if (common.isEmpty) return -1
    }
    common.min
  }
}
