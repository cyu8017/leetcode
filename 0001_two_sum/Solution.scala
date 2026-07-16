// LeetCode 0001 - Two Sum
// https://leetcode.com/problems/two-sum/

object Solution {
  def twoSum(nums: Array[Int], target: Int): Array[Int] = {
    val seen = scala.collection.mutable.Map.empty[Int, Int]
    nums.indices.foreach { i =>
      val complement = target - nums(i)
      if (seen.contains(complement)) {
        return Array(seen(complement), i)
      }
      seen(nums(i)) = i
    }
    Array.empty[Int]
  }
}
