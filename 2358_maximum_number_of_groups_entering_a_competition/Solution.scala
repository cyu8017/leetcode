// LeetCode 2358 - Maximum Number of Groups Entering a Competition
// https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/

object Solution {
  def maximumGroups(grades: Array[Int]): Int = {
    val n = grades.length
    var k = 0
    while ((k + 1L) * (k + 2) / 2 <= n) k += 1
    k
  }
}
