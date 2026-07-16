// LeetCode 0016 - 3Sum Closest
// https://leetcode.com/problems/3sum-closest/

object Solution {
  def threeSumClosest(nums: Array[Int], target: Int): Int = {
    val sorted = nums.sorted
    var closest = sorted(0) + sorted(1) + sorted(2)

    var i = 0
    while (i < sorted.length - 2) {
      var left = i + 1
      var right = sorted.length - 1
      while (left < right) {
        val total = sorted(i) + sorted(left) + sorted(right)
        if (math.abs(total - target) < math.abs(closest - target)) {
          closest = total
        }
        if (total < target) {
          left += 1
        } else if (total > target) {
          right -= 1
        } else {
          return total
        }
      }
      i += 1
    }

    closest
  }
}
