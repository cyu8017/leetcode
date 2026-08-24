// LeetCode 3741 - Minimum Distance Between Three Equal Elements II
// https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/

object Solution {
  def minimumDistance(nums: Array[Int]): Int = {
    val g = new java.util.HashMap[Integer, java.util.List[Integer]]()
    var i = 0
    while (i < nums.length) {
      g.computeIfAbsent(nums(i), _ => new java.util.ArrayList[Integer]()).add(i)
      i += 1
    }
    val inf = 1 << 30
    var ans = inf
    val it = g.values().iterator()
    while (it.hasNext) {
      val ls = it.next()
      val m = ls.size()
      var h = 0
      while (h < m - 2) {
        ans = math.min(ans, (ls.get(h + 2) - ls.get(h)) * 2)
        h += 1
      }
    }
    if (ans == inf) -1 else ans
  }
}
