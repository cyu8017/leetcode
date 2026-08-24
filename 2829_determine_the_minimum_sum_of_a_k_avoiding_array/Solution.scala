// LeetCode 2829 - Determine the Minimum Sum of a k-avoiding Array
// https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/

object Solution {
  def minimumSum(n: Int, k: Int): Int = {
    val used = scala.collection.mutable.HashSet.empty[Int]
    var sum = 0
    var x = 1
    while (used.size < n) {
      if (!used.contains(k - x)) {
        used += x
        sum += x
      }
      x += 1
    }
    sum
  }
}
