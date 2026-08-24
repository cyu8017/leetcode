// LeetCode 3814 - Maximum Capacity Within Budget
// https://leetcode.com/problems/maximum-capacity-within-budget/

object Solution {
  def maxCapacity(costs: Array[Int], capacity: Array[Int], budget: Int): Int = {
    val arr = new java.util.ArrayList[Array[Int]]()
    var k = 0
    while (k < costs.length) {
      if (costs(k) < budget) arr.add(Array(costs(k), capacity(k)))
      k += 1
    }
    if (arr.isEmpty) return 0
    arr.sort((a: Array[Int], b: Array[Int]) => Integer.compare(a(0), b(0)))
    val m = arr.size()
    val alive = Array.fill(m)(true)
    val h = new java.util.PriorityQueue[Array[Int]]((a: Array[Int], b: Array[Int]) => {
      if (a(0) != b(0)) Integer.compare(b(0), a(0))
      else Integer.compare(b(1), a(1))
    })
    var i = 0
    while (i < m) {
      h.offer(Array(arr.get(i)(1), i))
      i += 1
    }
    while (!h.isEmpty && !alive(h.peek()(1))) h.poll()
    var ans = h.peek()(0)
    i = 0
    var j = m - 1
    while (i < j) {
      alive(i) = false
      while (i < j && arr.get(i)(0) + arr.get(j)(0) >= budget) {
        alive(j) = false
        j -= 1
      }
      while (!h.isEmpty && !alive(h.peek()(1))) h.poll()
      if (!h.isEmpty) ans = math.max(ans, arr.get(i)(1) + h.peek()(0))
      i += 1
    }
    ans
  }
}
