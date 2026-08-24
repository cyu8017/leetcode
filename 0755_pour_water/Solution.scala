// LeetCode 0755 - Pour Water
// https://leetcode.com/problems/pour-water/

object Solution {
  def pourWater(heights: Array[Int], volume: Int, k: Int): Array[Int] = {
    var v = 0
    while (v < volume) {
      var index = k
      var i = k - 1
      while (i >= 0) {
        if (heights(i) > heights(index)) i = -1
        else {
          if (heights(i) < heights(index)) index = i
          i -= 1
        }
      }
      if (index != k) heights(index) += 1
      else {
        index = k
        i = k + 1
        while (i < heights.length) {
          if (heights(i) > heights(index)) i = heights.length
          else {
            if (heights(i) < heights(index)) index = i
            i += 1
          }
        }
        heights(index) += 1
      }
      v += 1
    }
    heights
  }
}
