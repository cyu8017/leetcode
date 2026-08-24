// LeetCode 3709 - Design Exam Scores Tracker
// https://leetcode.com/problems/design-exam-scores-tracker/

class ExamTracker {
    private val times = ArrayList<Int>()
    private val pre = ArrayList<Long>()

    init {
        times.add(0)
        pre.add(0L)
    }

    fun record(time: Int, score: Int) {
        times.add(time)
        pre.add(pre[pre.size - 1] + score)
    }

    fun totalScore(startTime: Int, endTime: Int): Long {
        val l = lowerBound(times, startTime) - 1
        val r = lowerBound(times, endTime + 1) - 1
        return pre[r] - pre[l]
    }

    private fun lowerBound(a: MutableList<Int>, target: Int): Int {
        var lo = 0
        var hi = a.size
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (a[mid] < target) lo = mid + 1
            else hi = mid
        }
        return lo
    }
}
