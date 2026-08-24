// LeetCode 0947 - Most Stones Removed with Same Row or Column
// https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

object Solution {
  def removeStones(stones: Array[Array[Int]]): Int = {
    val parent = scala.collection.mutable.Map.empty[Int, Int]
    def find(x: Int): Int = {
      if (!parent.contains(x)) parent(x) = x
      if (parent(x) != x) parent(x) = find(parent(x))
      parent(x)
    }
    def unite(a: Int, b: Int): Unit = { parent(find(a)) = find(b) }
    stones.foreach { s => unite(s(0), ~s(1)) }
    val roots = scala.collection.mutable.Set.empty[Int]
    stones.foreach { s => roots += find(s(0)) }
    stones.length - roots.size
  }
}
