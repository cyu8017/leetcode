// LeetCode 1748 - Sum of Unique Elements
// https://leetcode.com/problems/sum-of-unique-elements/

object Solution {
  def sumOfUnique(nums: Array[Int]): Int = {
    val counts = scala.collection.mutable.Map.empty[Int, Int].withDefaultValue(0)
    nums.foreach { value =>
      counts(value) += 1
    }
    counts.collect { case (value, count) if count == 1 => value }.sum
  }
}
