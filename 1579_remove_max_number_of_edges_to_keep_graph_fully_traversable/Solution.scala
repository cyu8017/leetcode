// LeetCode 1579 - Remove Max Number of Edges to Keep Graph Fully Traversable
// https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

object Solution {
  private class DSU(n: Int) {
    private val parent = Array.tabulate(n + 1)(identity)
    var components: Int = n
    def find(x: Int): Int = {
      var cur = x
      while (cur != parent(cur)) {
        parent(cur) = parent(parent(cur))
        cur = parent(cur)
      }
      cur
    }
    def union(a0: Int, b0: Int): Boolean = {
      val a = find(a0)
      val b = find(b0)
      if (a == b) false
      else {
        parent(a) = b
        components -= 1
        true
      }
    }
  }

  def maxNumEdgesToRemove(n: Int, edges: Array[Array[Int]]): Int = {
    val alice = new DSU(n)
    val bob = new DSU(n)
    var used = 0
    for (Array(t, u, v) <- edges if t == 3) {
      val merged = alice.union(u, v)
      bob.union(u, v)
      if (merged) used += 1
    }
    for (Array(t, u, v) <- edges) {
      if (t == 1) { if (alice.union(u, v)) used += 1 }
      else if (t == 2) { if (bob.union(u, v)) used += 1 }
    }
    if (alice.components == 1 && bob.components == 1) edges.length - used else -1
  }
}
