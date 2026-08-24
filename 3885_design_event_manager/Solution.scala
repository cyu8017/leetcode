// LeetCode 3885 - Design Event Manager
// https://leetcode.com/problems/design-event-manager/

class EventManager(events: Array[Array[Int]]) {
  private val sl = scala.collection.mutable.TreeSet.empty[(Long, Long)]
  private val d = scala.collection.mutable.Map.empty[Int, Int]

  events.foreach { e =>
    val eventId = e(0)
    val priority = e(1)
    sl += ((-priority.toLong, eventId.toLong))
    d(eventId) = priority
  }

  def updatePriority(eventId: Int, newPriority: Int): Unit = {
    val old = d(eventId)
    sl -= ((-old.toLong, eventId.toLong))
    sl += ((-newPriority.toLong, eventId.toLong))
    d(eventId) = newPriority
  }

  def pollHighest(): Int = {
    if (sl.isEmpty) return -1
    val top = sl.head
    sl -= top
    d.remove(top._2.toInt)
    top._2.toInt
  }
}
