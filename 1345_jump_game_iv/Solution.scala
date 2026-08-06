import scala.collection.mutable

object Solution {
  def minJumps(arr: Array[Int]): Int = {
    val positions = mutable.Map.empty[Int, mutable.ArrayBuffer[Int]]
    arr.indices.foreach(i => positions.getOrElseUpdate(arr(i), mutable.ArrayBuffer.empty) += i)
    val seen = Array.fill(arr.length)(false); val queue = mutable.Queue(0); seen(0) = true
    var steps = 0
    while (queue.nonEmpty) {
      for (_ <- queue.indices) {
        val i = queue.dequeue()
        if (i == arr.length - 1) return steps
        val neighbors = positions.remove(arr(i)).getOrElse(mutable.ArrayBuffer.empty) ++ Seq(i - 1, i + 1)
        neighbors.foreach(j => if (j >= 0 && j < arr.length && !seen(j)) { seen(j) = true; queue.enqueue(j) })
      }
      steps += 1
    }
    -1
  }
}
