object Solution {
  def findMaxValueOfEquation(points: Array[Array[Int]], k: Int): Int = {
    val queue = new java.util.ArrayDeque[Array[Int]]()
    var answer = Int.MinValue
    for (point <- points) {
      val x = point(0)
      val y = point(1)
      while (!queue.isEmpty && x - queue.peekFirst()(0) > k) queue.removeFirst()
      if (!queue.isEmpty) answer = math.max(answer, x + y + queue.peekFirst()(1))
      val value = y - x
      while (!queue.isEmpty && queue.peekLast()(1) <= value) queue.removeLast()
      queue.addLast(Array(x, value))
    }
    answer
  }
}
