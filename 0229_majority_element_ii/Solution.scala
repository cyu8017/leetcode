// LeetCode 0229 - Majority Element II
// https://leetcode.com/problems/majority-element-ii/

import scala.collection.mutable

object Solution {
  def majorityElement(nums: Array[Int]): List[Int] = {
    var candidate1: Option[Int] = None
    var candidate2: Option[Int] = None
    var count1 = 0
    var count2 = 0

    for (num <- nums) {
      if (candidate1.contains(num)) {
        count1 += 1
      } else if (candidate2.contains(num)) {
        count2 += 1
      } else if (count1 == 0) {
        candidate1 = Some(num)
        count1 = 1
      } else if (count2 == 0) {
        candidate2 = Some(num)
        count2 = 1
      } else {
        count1 -= 1
        count2 -= 1
      }
    }

    count1 = 0
    count2 = 0
    for (num <- nums) {
      if (candidate1.contains(num)) {
        count1 += 1
      } else if (candidate2.contains(num)) {
        count2 += 1
      }
    }

    val threshold = nums.length / 3
    val result = mutable.ArrayBuffer.empty[Int]
    if (count1 > threshold) {
      result += candidate1.get
    }
    if (candidate2.isDefined && candidate2 != candidate1 && count2 > threshold) {
      result += candidate2.get
    }
    result.toList
  }
}
