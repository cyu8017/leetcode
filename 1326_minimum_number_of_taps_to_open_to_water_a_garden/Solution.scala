// LeetCode 1326 - Minimum Number of Taps to Open to Water a Garden
// https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/

object Solution {
  def minTaps(n: Int, ranges: Array[Int]): Int = {
    val farthest = Array.ofDim[Int](n + 1)
    for (center <- ranges.indices) {
      val radius = ranges(center)
      val left = math.max(0, center - radius)
      val right = math.min(n, center + radius)
      farthest(left) = math.max(farthest(left), right)
    }
    var taps = 0
    var end = 0
    var reach = 0
    for (position <- 0 until n) {
      reach = math.max(reach, farthest(position))
      if (position == end) {
        if (reach <= position) return -1
        taps += 1
        end = reach
      }
    }
    taps
  }
}
