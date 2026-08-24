// LeetCode 3492 - Maximum Containers on a Ship
// https://leetcode.com/problems/maximum-containers-on-a-ship/

object Solution {
  def maxContainers(n: Int, w: Int, maxWeight: Int): Int = {
    val cap = n * n
    val byW = maxWeight / w
    if (cap < byW) cap else byW
  }
}
