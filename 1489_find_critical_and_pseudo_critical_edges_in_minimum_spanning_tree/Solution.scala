object Solution {
  def findCriticalAndPseudoCriticalEdges(n: Int, edges: Array[Array[Int]]): List[List[Int]] = {
    val sorted = edges.zipWithIndex.map { case (edge, index) => Array(edge(2), edge(0), edge(1), index) }.sortBy(_(0))
    def mst(skip: Int = -1, force: Int = -1): Long = {
      val parent = Array.tabulate(n)(identity)
      def find(node: Int): Int = {
        var current = node
        while (current != parent(current)) {
          parent(current) = parent(parent(current))
          current = parent(current)
        }
        current
      }
      var total = 0L
      var used = 0
      if (force >= 0) {
        val edge = sorted(force)
        parent(find(edge(1))) = find(edge(2))
        total += edge(0)
        used += 1
      }
      for (i <- sorted.indices if i != skip && i != force) {
        val edge = sorted(i)
        val left = find(edge(1))
        val right = find(edge(2))
        if (left != right) {
          parent(left) = right
          total += edge(0)
          used += 1
        }
      }
      if (used == n - 1) total else Long.MaxValue / 4
    }
    val base = mst()
    val critical = scala.collection.mutable.ListBuffer.empty[Int]
    val pseudo = scala.collection.mutable.ListBuffer.empty[Int]
    for (i <- sorted.indices) {
      if (mst(skip = i) > base) critical += sorted(i)(3)
      else if (mst(force = i) == base) pseudo += sorted(i)(3)
    }
    List(critical.sorted.toList, pseudo.sorted.toList)
  }
}
