// LeetCode 0841 - Keys and Rooms
// https://leetcode.com/problems/keys-and-rooms/

object Solution {
  def canVisitAllRooms(rooms: List[List[Int]]): Boolean = {
    val seen = scala.collection.mutable.Set(0)
    val stack = scala.collection.mutable.ArrayDeque(0)
    while (stack.nonEmpty) {
      val room = stack.removeLast()
      rooms(room).foreach { key =>
        if (seen.add(key)) stack.append(key)
      }
    }
    seen.size == rooms.length
  }
}
