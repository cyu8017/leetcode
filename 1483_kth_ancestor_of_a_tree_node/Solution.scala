class TreeAncestor(n: Int, parent: Array[Int]) {
  private val up = scala.collection.mutable.ArrayBuffer(parent.clone())
  private val width = math.max(1, 32 - Integer.numberOfLeadingZeros(n))
  for (bit <- 1 until width) {
    val previous = up(bit - 1)
    up += Array.tabulate(n)(node => if (previous(node) == -1) -1 else previous(previous(node)))
  }

  def getKthAncestor(node: Int, k: Int): Int = {
    var current = node
    var steps = k
    var bit = 0
    while (steps > 0 && current != -1) {
      if ((steps & 1) != 0) {
        if (bit >= up.length) return -1
        current = up(bit)(current)
      }
      bit += 1
      steps >>= 1
    }
    current
  }
}
