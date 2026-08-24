// LeetCode 3069 - Distribute Elements Into Two Arrays I
// https://leetcode.com/problems/distribute-elements-into-two-arrays-i/

object Solution {
  def resultArray(nums: Array[Int]): Array[Int] = {
    val arr1 = scala.collection.mutable.ArrayBuffer(nums(0))
    val arr2 = scala.collection.mutable.ArrayBuffer(nums(1))
    var i = 2
    while (i < nums.length) {
      if (arr1.last > arr2.last) arr1 += nums(i)
      else arr2 += nums(i)
      i += 1
    }
    (arr1 ++ arr2).toArray
  }
}
