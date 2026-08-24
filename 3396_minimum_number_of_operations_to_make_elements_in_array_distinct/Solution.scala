// LeetCode 3396 - Minimum Number of Operations to Make Elements in Array Distinct
// https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

object Solution {
  def minimumOperations(nums: Array[Int]): Int = {
    val list = scala.collection.mutable.ArrayBuffer.from(nums)
    var ops = 0
    while (true) {
      val seen = scala.collection.mutable.Set.empty[Int]
      var dup = false
      list.foreach { x =>
        if (!dup && !seen.add(x)) dup = true
      }
      if (!dup) return ops
      if (list.size <= 3) return ops + 1
      list.remove(0, 3)
      ops += 1
    }
    ops
  }
}
