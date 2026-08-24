// LeetCode 3383 - Minimum Runes to Add to Cast Spell
// https://leetcode.com/problems/minimum-runes-to-add-to-cast-spell/

object Solution {
  def minRunesToAdd(n: Int, crystals: Array[Int], flowFrom: Array[Int], flowTo: Array[Int]): Int = {
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    val rg = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    var i = 0
    while (i < flowFrom.length) {
      val a = flowFrom(i)
      val b = flowTo(i)
      g(a) += b
      rg(b) += a
      i += 1
    }
    val vis = new Array[Boolean](n)
    val order = scala.collection.mutable.ArrayBuffer.empty[Int]
    def dfs1(u: Int): Unit = {
      vis(u) = true
      for (v <- g(u)) if (!vis(v)) dfs1(v)
      order += u
    }
    i = 0
    while (i < n) {
      if (!vis(i)) dfs1(i)
      i += 1
    }
    val comp = Array.fill(n)(-1)
    var cid = 0
    def dfs2(u: Int): Unit = {
      comp(u) = cid
      for (v <- rg(u)) if (comp(v) == -1) dfs2(v)
    }
    i = n - 1
    while (i >= 0) {
      val u = order(i)
      if (comp(u) == -1) {
        dfs2(u)
        cid += 1
      }
      i -= 1
    }
    val hasCrystal = new Array[Boolean](cid)
    for (c <- crystals) hasCrystal(comp(c)) = true
    val indeg = new Array[Int](cid)
    var u = 0
    while (u < n) {
      for (v <- g(u)) {
        if (comp(u) != comp(v)) indeg(comp(v)) += 1
      }
      u += 1
    }
    var ans = 0
    i = 0
    while (i < cid) {
      if (indeg(i) == 0 && !hasCrystal(i)) ans += 1
      i += 1
    }
    ans
  }
}
