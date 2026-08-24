// LeetCode 2102 - Sequentially Ordinal Rank Tracker
// https://leetcode.com/problems/sequentially-ordinal-rank-tracker/

import java.util.PriorityQueue

class SORTracker {
    private data class Loc(val name: String, val score: Int)

    private val best = PriorityQueue<Loc> { a, b ->
        if (a.score != b.score) a.score.compareTo(b.score)
        else b.name.compareTo(a.name)
    }
    private val rest = PriorityQueue<Loc> { a, b ->
        if (a.score != b.score) b.score.compareTo(a.score)
        else a.name.compareTo(b.name)
    }
    private var k = 0

    fun add(name: String, score: Int) {
        best.offer(Loc(name, score))
        if (best.size > k) rest.offer(best.poll())
    }

    fun get(): String {
        k++
        if (rest.isNotEmpty()) best.offer(rest.poll())
        return best.peek().name
    }
}
