// LeetCode 0075 - Sort Colors
// https://leetcode.com/problems/sort-colors/

object Solution {
  def sortColors(nums: Array[Int]): Unit = {
    var low = 0
    var mid = 0
    var high = nums.length - 1

    while (mid <= high) {
      nums(mid) match {
        case 0 =>
          val tmp = nums(low)
          nums(low) = nums(mid)
          nums(mid) = tmp
          low += 1
          mid += 1
        case 1 =>
          mid += 1
        case _ =>
          val tmp = nums(mid)
          nums(mid) = nums(high)
          nums(high) = tmp
          high -= 1
      }
    }
  }
}
