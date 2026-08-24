// LeetCode 2089 - Find Target Indices After Sorting Array
// https://leetcode.com/problems/find-target-indices-after-sorting-array/

object Solution {
  def targetIndices(nums: Array[Int], target: Int): List[Int] = {
    var less = 0
    var eq = 0
    nums.foreach { x =>
      if (x < target) less += 1
      else if (x == target) eq += 1
    }
    (0 until eq).map(i => less + i).toList
  }
}
