// LeetCode 0961 - N-Repeated Element in Size 2N Array
// https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

object Solution {
  def repeatedNTimes(nums: Array[Int]): Int = {
    val seen = scala.collection.mutable.Set.empty[Int]
    nums.foreach { x =>
      if (seen.contains(x)) return x
      seen += x
    }
    -1
  }
}
