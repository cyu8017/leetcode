// LeetCode 2855 - Minimum Right Shifts to Sort the Array
// https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/

object Solution {
  def minimumRightShifts(nums: Array[Int]): Int = {
    val n = nums.length
    var drops = 0
    var idx = -1
    for (i <- 0 until n) {
      if (nums(i) > nums((i + 1) % n)) {
        drops += 1
        idx = i
      }
    }
    if (drops == 0) 0
    else if (drops > 1) -1
    else n - 1 - idx
  }
}
