// LeetCode 1756 - Design Most Recently Used Queue
// https://leetcode.com/problems/design-most-recently-used-queue/

class MRUQueue(n: Int) {
    private val q = ArrayList<Int>(n)

    init {
        for (i in 1..n) {
            q.add(i)
        }
    }

    fun fetch(k: Int): Int {
        val value = q.removeAt(k - 1)
        q.add(value)
        return value
    }
}
