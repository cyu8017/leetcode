// LeetCode 0815 - Bus Routes
// https://leetcode.com/problems/bus-routes/

object Solution {
  def numBusesToDestination(routes: Array[Array[Int]], source: Int, target: Int): Int = {
    if (source == target) return 0
    val stopToBuses = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ListBuffer[Int]]
    routes.indices.foreach { bus =>
      routes(bus).foreach { stop =>
        stopToBuses.getOrElseUpdate(stop, scala.collection.mutable.ListBuffer.empty) += bus
      }
    }
    val queue = scala.collection.mutable.Queue[(Int, Int)]((source, 0))
    val seenStops = scala.collection.mutable.Set(source)
    val seenBuses = scala.collection.mutable.Set.empty[Int]
    while (queue.nonEmpty) {
      val (stop, busesTaken) = queue.dequeue()
      stopToBuses.getOrElse(stop, scala.collection.mutable.ListBuffer.empty[Int]).foreach { bus =>
        if (seenBuses.add(bus)) {
          routes(bus).foreach { nxt =>
            if (nxt == target) return busesTaken + 1
            if (seenStops.add(nxt)) queue.enqueue((nxt, busesTaken + 1))
          }
        }
      }
    }
    -1
  }
}
