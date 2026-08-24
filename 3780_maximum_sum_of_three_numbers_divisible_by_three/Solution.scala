// LeetCode 3780 - Maximum Sum Of Three Numbers Divisible By Three
// https://leetcode.com/problems/maximum-sum-of-three-numbers-divisible-by-three/

object Solution {
  def maximumSum(nums: Array[Int]): Int = {
    java.util.Arrays.sort(nums)
    val g = Array.fill(3)(new java.util.ArrayList[Integer]())
    nums.foreach(x => g(x % 3).add(x))
    var ans = 0
    var a = 0
    while (a < 3) {
      if (!g(a).isEmpty) {
        val x = g(a).remove(g(a).size() - 1)
        var b = 0
        while (b < 3) {
          if (!g(b).isEmpty) {
            val y = g(b).remove(g(b).size() - 1)
            val c = (3 - (a + b) % 3) % 3
            if (!g(c).isEmpty) {
              val z = g(c).get(g(c).size() - 1)
              ans = math.max(ans, x + y + z)
            }
            g(b).add(y)
          }
          b += 1
        }
        g(a).add(x)
      }
      a += 1
    }
    ans
  }
}
