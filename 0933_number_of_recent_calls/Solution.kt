// LeetCode 0933 - Number of Recent Calls
// https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter {
    private val q = ArrayDeque<Int>()

    fun ping(t: Int): Int {
        q.add(t)
        while (q.first() < t - 3000) q.removeFirst()
        return q.size
    }
}
