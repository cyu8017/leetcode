// LeetCode 3885 - Design Event Manager
// https://leetcode.com/problems/design-event-manager/

class EventManager(events: Array<IntArray>) {
    private val sl = sortedSetOf<Pair<Long, Long>>(compareBy({ it.first }, { it.second }))
    private val d = HashMap<Int, Int>()

    init {
        for (e in events) {
            val eventId = e[0]
            val priority = e[1]
            sl.add((-priority.toLong()) to eventId.toLong())
            d[eventId] = priority
        }
    }

    fun updatePriority(eventId: Int, newPriority: Int) {
        val old = d[eventId]!!
        sl.remove((-old.toLong()) to eventId.toLong())
        sl.add((-newPriority.toLong()) to eventId.toLong())
        d[eventId] = newPriority
    }

    fun pollHighest(): Int {
        if (sl.isEmpty()) return -1
        val top = sl.first()
        val eventId = top.second.toInt()
        sl.remove(top)
        d.remove(eventId)
        return eventId
    }
}
