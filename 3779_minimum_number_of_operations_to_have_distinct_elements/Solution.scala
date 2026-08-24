// LeetCode 3779 - Minimum Number Of Operations To Have Distinct Elements
// https://leetcode.com/problems/minimum-number-of-operations-to-have-distinct-elements/

object Solution {
  def minOperations(nums: Array[Int]): Int = {
    val st = new java.util.HashSet[Integer]()
    var i = nums.length - 1
    while (i >= 0) {
      if (st.contains(nums(i))) return i / 3 + 1
      st.add(nums(i))
      i -= 1
    }
    0
  }
}
