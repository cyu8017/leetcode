// LeetCode 3784 - Minimum Deletion Cost To Make All Characters Equal
// https://leetcode.com/problems/minimum-deletion-cost-to-make-all-characters-equal/

object Solution {
  def minCost(s: String, cost: Array[Int]): Long = {
    var tot = 0L
    val g = new java.util.HashMap[Character, java.lang.Long]()
    var i = 0
    while (i < cost.length) {
      tot += cost(i)
      g.merge(s.charAt(i), cost(i).toLong, (a: java.lang.Long, b: java.lang.Long) => java.lang.Long.valueOf(a + b))
      i += 1
    }
    var ans = tot
    val it = g.values().iterator()
    while (it.hasNext) {
      val x = it.next()
      ans = math.min(ans, tot - x)
    }
    ans
  }
}
