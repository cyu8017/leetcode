// LeetCode 1847 - Closest Room
// https://leetcode.com/problems/closest-room/

object Solution {
  def closestRoom(rooms: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
    val sortedRooms = rooms.sortBy(_(1))
    val indexed = queries.indices.map(i => (i, queries(i)(0), queries(i)(1))).sortBy(-_._3)
    val available = scala.collection.mutable.SortedSet.empty[Int]
    var roomIndex = sortedRooms.length - 1
    val answer = Array.fill(queries.length)(-1)

    for ((queryIndex, preferred, minSize) <- indexed) {
      while (roomIndex >= 0 && sortedRooms(roomIndex)(1) >= minSize) {
        available += sortedRooms(roomIndex)(0)
        roomIndex -= 1
      }
      if (available.nonEmpty) {
        val ge = available.rangeFrom(preferred)
        val le = available.rangeTo(preferred)
        var bestId = -1
        var bestDist = Int.MaxValue
        if (ge.nonEmpty) {
          val roomId = ge.head
          val dist = math.abs(roomId - preferred)
          if (dist < bestDist || (dist == bestDist && roomId < bestId)) {
            bestId = roomId
            bestDist = dist
          }
        }
        if (le.nonEmpty) {
          val roomId = le.last
          val dist = math.abs(roomId - preferred)
          if (dist < bestDist || (dist == bestDist && roomId < bestId)) {
            bestId = roomId
          }
        }
        answer(queryIndex) = bestId
      }
    }
    answer
  }
}
