// LeetCode 1762 - Buildings With an Ocean View
// https://leetcode.com/problems/buildings-with-an-ocean-view/

object Solution {
  def findBuildings(heights: Array[Int]): Array[Int] = {
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    var tallest = 0
    for (i <- heights.indices.reverse) {
      if (heights(i) > tallest) {
        ans += i
        tallest = heights(i)
      }
    }
    ans.reverse.toArray
  }
}
