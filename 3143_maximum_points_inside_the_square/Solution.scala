// LeetCode 3143 - Maximum Points Inside the Square
// https://leetcode.com/problems/maximum-points-inside-the-square/

object Solution {
  def maxPointsInsideSquare(points: Array[Array[Int]], s: String): Int = {
    val g = new java.util.TreeMap[Integer, java.util.List[Integer]]()
    var i = 0
    while (i < points.length) {
      val key = math.max(math.max(points(i)(0), -points(i)(0)), math.max(points(i)(1), -points(i)(1)))
      g.computeIfAbsent(key, (_: Integer) => new java.util.ArrayList[Integer]()).add(i)
      i += 1
    }
    val vis = new Array[Boolean](26)
    var ans = 0
    val it = g.entrySet().iterator()
    while (it.hasNext) {
      val e = it.next()
      val vals = e.getValue
      var vi = 0
      while (vi < vals.size()) {
        val idx = vals.get(vi)
        val j = s.charAt(idx) - 'a'
        if (vis(j)) return ans
        vis(j) = true
        vi += 1
      }
      ans += vals.size()
    }
    ans
  }
}
