// LeetCode 3661 - Maximum Walls Destroyed by Robots
// https://leetcode.com/problems/maximum-walls-destroyed-by-robots/

object Solution {
  def maxWalls(robots: Array[Int], distance: Array[Int], walls: Array[Int]): Int = {
    val n = robots.length
    val arr = Array.ofDim[Int](n, 2)
    var i = 0
    while (i < n) {
      arr(i)(0) = robots(i)
      arr(i)(1) = distance(i)
      i += 1
    }
    java.util.Arrays.sort(arr, (a: Array[Int], b: Array[Int]) => Integer.compare(a(0), b(0)))
    java.util.Arrays.sort(walls)
    val memo = new java.util.HashMap[java.lang.Long, Integer]()

    def lowerBound(a: Array[Int], target: Int): Int = {
      var lo = 0
      var hi = a.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (a(mid) < target) lo = mid + 1
        else hi = mid
      }
      lo
    }

    def dfs(ii: Int, j: Int): Int = {
      if (ii < 0) return 0
      val key = (ii.toLong << 1) | j
      if (memo.containsKey(key)) return memo.get(key)
      var left = arr(ii)(0) - arr(ii)(1)
      if (ii > 0) left = math.max(left, arr(ii - 1)(0) + 1)
      var l = lowerBound(walls, left)
      var r = lowerBound(walls, arr(ii)(0) + 1)
      var ans = dfs(ii - 1, 0) + (r - l)
      var right = arr(ii)(0) + arr(ii)(1)
      if (ii + 1 < arr.length) {
        if (j == 0) right = math.min(right, arr(ii + 1)(0) - arr(ii + 1)(1) - 1)
        else right = math.min(right, arr(ii + 1)(0) - 1)
      }
      l = lowerBound(walls, arr(ii)(0))
      r = lowerBound(walls, right + 1)
      ans = math.max(ans, dfs(ii - 1, 1) + (r - l))
      memo.put(key, ans)
      ans
    }
    dfs(n - 1, 1)
  }
}
