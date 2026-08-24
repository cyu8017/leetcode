// LeetCode 3516 - Find Closest Person
// https://leetcode.com/problems/find-closest-person/

object Solution {
  def findClosest(x: Int, y: Int, z: Int): Int = {
    val a = math.abs(x - z)
    val b = math.abs(y - z)
    if (a == b) 0 else if (a < b) 1 else 2
  }
}
