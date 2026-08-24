// LeetCode 3645 - Maximum Total from Optimal Activation Order
// https://leetcode.com/problems/maximum-total-from-optimal-activation-order/

object Solution {
  def maxTotal(value: Array[Int], limit: Array[Int]): Long = {
    val g = new java.util.HashMap[Integer, java.util.List[Integer]]()
    var i = 0
    while (i < value.length) {
      g.computeIfAbsent(limit(i), _ => new java.util.ArrayList[Integer]()).add(value(i))
      i += 1
    }
    var ans = 0L
    val it = g.entrySet().iterator()
    while (it.hasNext) {
      val e = it.next()
      val lim = e.getKey.intValue()
      val vs = e.getValue
      vs.sort(java.util.Collections.reverseOrder())
      i = 0
      while (i < math.min(lim, vs.size())) {
        ans += vs.get(i)
        i += 1
      }
    }
    ans
  }
}
