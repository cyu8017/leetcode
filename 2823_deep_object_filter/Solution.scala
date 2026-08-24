// LeetCode 2823 - Deep Object Filter
// https://leetcode.com/problems/deep-object-filter/

object Solution {
  def deepFilter(obj: Array[Int], fn: Int => Boolean): List[Int] =
    obj.filter(fn).toList
}
