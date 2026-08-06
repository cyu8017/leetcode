import scala.collection.mutable
object Solution {
  def kthSmallest(mat: Array[Array[Int]], k: Int): Int = {
    var sums = Array(0)
    for (row <- mat) {
      implicit val ordering: Ordering[(Int, Int, Int)] = Ordering.by[(Int, Int, Int), Int](-_._1)
      val heap = mutable.PriorityQueue((sums(0) + row(0), 0, 0))
      val merged = mutable.ArrayBuffer.empty[Int]
      while (heap.nonEmpty && merged.length < k) {
        val (value, i, j) = heap.dequeue(); merged += value
        if (j + 1 < row.length) heap.enqueue((sums(i) + row(j + 1), i, j + 1))
        if (j == 0 && i + 1 < sums.length) heap.enqueue((sums(i + 1) + row(0), i + 1, 0))
      }
      sums = merged.toArray
    }
    sums(k - 1)
  }
}
