// LeetCode 1296 - Divide Array in Sets of K Consecutive Numbers
// https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

object Solution {
  def isPossibleDivide(nums: Array[Int], k: Int): Boolean = {
    if (nums.length % k != 0) return false
    val counts = scala.collection.mutable.TreeMap.empty[Int, Int].withDefaultValue(0)
    for (x <- nums) counts(x) += 1
    while (counts.nonEmpty) {
      val start = counts.firstKey
      val amount = counts(start)
      for (value <- start until start + k) {
        if (counts(value) < amount) return false
        counts(value) -= amount
        if (counts(value) == 0) counts.remove(value)
      }
    }
    true
  }
}
