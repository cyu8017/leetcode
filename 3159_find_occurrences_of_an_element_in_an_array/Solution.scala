// LeetCode 3159 - Find Occurrences of an Element in an Array
// https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/

object Solution {
  def occurrencesOfElement(nums: Array[Int], queries: Array[Int], x: Int): Array[Int] = {
    val ids = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < nums.length) {
      if (nums(i) == x) ids += i
      i += 1
    }
    Array.tabulate(queries.length) { qi =>
      val idx = queries(qi)
      if (idx - 1 < ids.size) ids(idx - 1) else -1
    }
  }
}
