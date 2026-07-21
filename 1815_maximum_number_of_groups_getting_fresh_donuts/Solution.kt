// LeetCode 1815 - Maximum Number of Groups Getting Fresh Donuts
// https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/

class Solution {
    fun maxHappyGroups(batchSize: Int, groups: IntArray): Int {
        val count = IntArray(batchSize)
        for (size in groups) count[size % batchSize]++

        val memo = HashMap<String, Int>()

        fun dfs(remainder: Int, state: IntArray): Int {
            val key = "$remainder|${state.joinToString(",")}"
            memo[key]?.let { return it }
            var best = 0
            for (mod in 1 until batchSize) {
                if (state[mod] == 0) continue
                state[mod]--
                best = maxOf(best, dfs((remainder + mod) % batchSize, state))
                state[mod]++
            }
            if (remainder == 0) best++
            memo[key] = best
            return best
        }

        var ans = dfs(0, count.copyOf())
        if (count[0] > 0) ans += count[0] - 1
        return ans
    }
}
