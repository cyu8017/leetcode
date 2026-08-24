// LeetCode 2440 - Create Components With Same Value
// https://leetcode.com/problems/create-components-with-same-value/

object Solution {
  def componentValue(nums: Array[Int], edges: Array[Array[Int]]): Int = {
    val n = nums.length
    var total = 0
    var i = 0
    while (i < n) { total += nums(i); i += 1 }
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }

    def dfs(u: Int, p: Int, target: Int): Int = {
      var sum = nums(u)
      g(u).foreach { v =>
        if (v != p) {
          val sub = dfs(v, u, target)
          if (sub < 0) return -1
          sum += sub
        }
      }
      if (sum > target) return -1
      if (sum == target) 0 else sum
    }

    var parts = n
    while (parts >= 1) {
      if (total % parts == 0) {
        val target = total / parts
        if (dfs(0, -1, target) == 0) return parts - 1
      }
      parts -= 1
    }
    0
  }
}
