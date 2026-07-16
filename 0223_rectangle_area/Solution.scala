// LeetCode 0223 - Rectangle Area
// https://leetcode.com/problems/rectangle-area/

object Solution {
  def computeArea(ax1: Int, ay1: Int, ax2: Int, ay2: Int, bx1: Int, by1: Int, bx2: Int, by2: Int): Int = {
    val areaA = (ax2 - ax1) * (ay2 - ay1)
    val areaB = (bx2 - bx1) * (by2 - by1)
    val overlapW = Math.max(0, Math.min(ax2, bx2) - Math.max(ax1, bx1))
    val overlapH = Math.max(0, Math.min(ay2, by2) - Math.max(ay1, by1))
    areaA + areaB - overlapW * overlapH
  }
}
