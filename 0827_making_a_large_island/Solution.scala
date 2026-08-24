// LeetCode 0827 - Making A Large Island
// https://leetcode.com/problems/making-a-large-island/

object Solution {
  def largestIsland(grid: Array[Array[Int]]): Int = {
    val n = grid.length
    val sizes = scala.collection.mutable.Map(0 -> 0)
    def dfs(r: Int, c: Int, iid: Int): Int = {
      if (r < 0 || r >= n || c < 0 || c >= n || grid(r)(c) != 1) return 0
      grid(r)(c) = iid
      1 + dfs(r + 1, c, iid) + dfs(r - 1, c, iid) + dfs(r, c + 1, iid) + dfs(r, c - 1, iid)
    }
    var islandId = 2
    var i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) == 1) {
          sizes(islandId) = dfs(i, j, islandId)
          islandId += 1
        }
        j += 1
      }
      i += 1
    }
    var ans = sizes.values.foldLeft(0)(math.max)
    val dr = Array(1, -1, 0, 0)
    val dc = Array(0, 0, 1, -1)
    i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) == 0) {
          val seen = scala.collection.mutable.Set.empty[Int]
          var total = 1
          var k = 0
          while (k < 4) {
            val ni = i + dr(k)
            val nj = j + dc(k)
            if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
              val iid = grid(ni)(nj)
              if (iid > 1 && seen.add(iid)) total += sizes(iid)
            }
            k += 1
          }
          ans = math.max(ans, total)
        }
        j += 1
      }
      i += 1
    }
    ans
  }
}
