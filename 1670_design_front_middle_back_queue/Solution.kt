// LeetCode 1670 - Design Front Middle Back Queue
// https://leetcode.com/problems/design-front-middle-back-queue/

class FrontMiddleBackQueue {
    private val l = ArrayDeque<Int>()
    private val r = ArrayDeque<Int>()

    private fun bal() {
        while (l.size > r.size + 1) r.addFirst(l.removeLast())
        while (r.size > l.size) l.addLast(r.removeFirst())
    }

    fun pushFront(`val`: Int) {
        l.addFirst(`val`)
        bal()
    }

    fun pushMiddle(`val`: Int) {
        if (l.size > r.size) r.addFirst(l.removeLast())
        l.addLast(`val`)
    }

    fun pushBack(`val`: Int) {
        r.addLast(`val`)
        bal()
    }

    fun popFront(): Int {
        if (l.isEmpty()) return -1
        val v = l.removeFirst()
        bal()
        return v
    }

    fun popMiddle(): Int {
        if (l.isEmpty()) return -1
        val v = l.removeLast()
        bal()
        return v
    }

    fun popBack(): Int {
        if (l.isEmpty()) return -1
        val v = if (r.isNotEmpty()) r.removeLast() else l.removeLast()
        bal()
        return v
    }
}
