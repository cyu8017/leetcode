// LeetCode 0219 - Contains Duplicate II
// https://leetcode.com/problems/contains-duplicate-ii/

import scala.collection.mutable

object Solution {
  def containsNearbyDuplicate(nums: Array[Int], k: Int): Boolean = {
    val lastIndex = mutable.Map.empty[Int, Int]
    for ((num, i) <- nums.zipWithIndex) {
      if (lastIndex.get(num).exists(prev => i - prev <= k)) {
        return true
      }
      lastIndex(num) = i
    }
    false
  }
}
