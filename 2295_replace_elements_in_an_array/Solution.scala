// LeetCode 2295 - Replace Elements in an Array
// https://leetcode.com/problems/replace-elements-in-an-array/

object Solution {
  def arrayChange(nums: Array[Int], operations: Array[Array[Int]]): Array[Int] = {
    val pos = scala.collection.mutable.HashMap.empty[Int, Int]
    var i = 0
    while (i < nums.length) {
      pos(nums(i)) = i
      i += 1
    }
    for (op <- operations) {
      val idx = pos(op(0))
      nums(idx) = op(1)
      pos.remove(op(0))
      pos(op(1)) = idx
    }
    nums
  }
}
