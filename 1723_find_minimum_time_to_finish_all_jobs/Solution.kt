// LeetCode 1723 - Find Minimum Time to Finish All Jobs
// https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/

class Solution {
    fun minimumTimeRequired(jobs: IntArray, k: Int): Int {
        val sorted = jobs.sortedDescending().toIntArray()
        val loads = IntArray(k)
        var best = sorted.sum()

        fun backtrack(i: Int) {
            if (i == sorted.size) {
                best = minOf(best, loads.maxOrNull()!!)
                return
            }
            val seen = HashSet<Int>()
            for (worker in 0 until k) {
                if (loads[worker] in seen) {
                    continue
                }
                if (loads[worker] + sorted[i] >= best) {
                    continue
                }
                seen.add(loads[worker])
                loads[worker] += sorted[i]
                backtrack(i + 1)
                loads[worker] -= sorted[i]
                if (loads[worker] == 0) {
                    break
                }
            }
        }

        backtrack(0)
        return best
    }
}
