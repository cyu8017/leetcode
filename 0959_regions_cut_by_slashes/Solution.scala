// LeetCode 0959 - Regions Cut By Slashes
// https://leetcode.com/problems/regions-cut-by-slashes/

object Solution {
  def regionsBySlashes(grid: Array[String]): Int = {
    val n = grid.length
    val parent = Array.tabulate(n * n * 4)(identity)
    def find(x: Int): Int = {
      if (parent(x) != x) parent(x) = find(parent(x))
      parent(x)
    }
    def unite(a: Int, b: Int): Unit = { parent(find(a)) = find(b) }
    var r = 0
    while (r < n) {
      var c = 0
      while (c < n) {
        val root = 4 * (r * n + c)
        val ch = grid(r).charAt(c)
        if (ch == '/') {
          unite(root + 0, root + 3)
          unite(root + 1, root + 2)
        } else if (ch == '\\') {
          unite(root + 0, root + 1)
          unite(root + 2, root + 3)
        } else {
          unite(root + 0, root + 1)
          unite(root + 1, root + 2)
          unite(root + 2, root + 3)
        }
        if (r + 1 < n) unite(root + 2, root + 4 * n + 0)
        if (c + 1 < n) unite(root + 1, root + 4 + 3)
        c += 1
      }
      r += 1
    }
    var ans = 0
    var i = 0
    while (i < parent.length) {
      if (find(i) == i) ans += 1
      i += 1
    }
    ans
  }
}
