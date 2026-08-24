// LeetCode 2127 - Maximum Employees to Be Invited to a Meeting
// https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/

object Solution {
  def maximumInvitations(favorite: Array[Int]): Int = {
    val n = favorite.length
    val indeg = Array.fill(n)(0)
    val depth = Array.fill(n)(1)
    favorite.foreach(f => indeg(f) += 1)
    val q = scala.collection.mutable.Queue[Int]()
    var i = 0
    while (i < n) {
      if (indeg(i) == 0) q.enqueue(i)
      i += 1
    }
    while (q.nonEmpty) {
      val u = q.dequeue()
      val v = favorite(u)
      depth(v) = math.max(depth(v), depth(u) + 1)
      indeg(v) -= 1
      if (indeg(v) == 0) q.enqueue(v)
    }
    var pairSum = 0
    var maxCycle = 0
    val vis = Array.fill(n)(false)
    i = 0
    while (i < n) {
      if (indeg(i) != 0 && !vis(i)) {
        var u = i
        var lenCycle = 0
        while (!vis(u)) {
          vis(u) = true
          u = favorite(u)
          lenCycle += 1
        }
        if (lenCycle == 2) pairSum += depth(i) + depth(favorite(i))
        else maxCycle = math.max(maxCycle, lenCycle)
      }
      i += 1
    }
    math.max(pairSum, maxCycle)
  }
}
