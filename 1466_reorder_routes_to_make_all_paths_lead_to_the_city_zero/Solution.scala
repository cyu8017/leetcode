object Solution {
  def minReorder(n: Int, connections: Array[Array[Int]]): Int = {
    val graph = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[(Int, Int)])
    for (edge <- connections) {
      graph(edge(0)) += ((edge(1), 1))
      graph(edge(1)) += ((edge(0), 0))
    }
    val seen = Array.fill(n)(false)
    val stack = scala.collection.mutable.Stack(0)
    seen(0) = true
    var answer = 0
    while (stack.nonEmpty) {
      val node = stack.pop()
      for ((neighbor, cost) <- graph(node) if !seen(neighbor)) {
        seen(neighbor) = true
        answer += cost
        stack.push(neighbor)
      }
    }
    answer
  }
}
