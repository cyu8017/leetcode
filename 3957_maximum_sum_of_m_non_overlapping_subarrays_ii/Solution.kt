// LeetCode 3957 - Maximum Sum of M Non-Overlapping Subarrays II
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-ii/

class Solution {
    private class State(var value: Long = 0, var count: Int = 0)

    private fun better(a: State, b: State): Boolean {
        return a.value > b.value || (a.value == b.value && a.count > b.count)
    }

    fun maxSum(nums: IntArray, m: Int, l: Int, r: Int): Long {
        val n = nums.size
        val prefix = LongArray(n + 1)
        for (i in 0 until n) prefix[i + 1] = prefix[i] + nums[i]
        val unconstrained = run(prefix, n, l, r, 0)
        if (unconstrained.count > 0 && unconstrained.count <= m) return unconstrained.value
        if (unconstrained.count > m) {
            var bound = 0L
            for (value in nums) bound += if (value >= 0) value.toLong() else (-value).toLong()
            var low = 0L
            var high = bound + 1
            while (low < high) {
                val mid = low + (high - low + 1) / 2
                if (run(prefix, n, l, r, mid).count >= m) low = mid else high = mid - 1
            }
            val state = run(prefix, n, l, r, low)
            return state.value + low * m
        }
        val infinity = 1L shl 60
        var bestSingle = -infinity
        val deque = ArrayDeque<Int>()
        for (end in 1..n) {
            val addIndex = end - l
            if (addIndex >= 0) {
                while (deque.isNotEmpty() && prefix[deque.last()] >= prefix[addIndex]) deque.removeLast()
                deque.addLast(addIndex)
            }
            val minIndex = end - r
            while (deque.isNotEmpty() && deque.first() < minIndex) deque.removeFirst()
            if (deque.isNotEmpty()) {
                val sum = prefix[end] - prefix[deque.first()]
                if (sum > bestSingle) bestSingle = sum
            }
        }
        return bestSingle
    }

    private fun run(prefix: LongArray, n: Int, l: Int, r: Int, penalty: Long): State {
        val dp = Array(n + 1) { State() }
        val deque = ArrayDeque<Int>()
        for (end in 1..n) {
            val addIndex = end - l
            if (addIndex >= 0) {
                while (deque.isNotEmpty() && candidateBetter(dp, prefix, addIndex, deque.last())) deque.removeLast()
                deque.addLast(addIndex)
            }
            val minIndex = end - r
            while (deque.isNotEmpty() && deque.first() < minIndex) deque.removeFirst()
            dp[end] = State(dp[end - 1].value, dp[end - 1].count)
            if (deque.isNotEmpty()) {
                val start = deque.first()
                val take = State(dp[start].value + prefix[end] - prefix[start] - penalty, dp[start].count + 1)
                if (better(take, dp[end])) dp[end] = take
            }
        }
        return dp[n]
    }

    private fun candidateBetter(dp: Array<State>, prefix: LongArray, a: Int, b: Int): Boolean {
        val left = State(dp[a].value - prefix[a], dp[a].count)
        val right = State(dp[b].value - prefix[b], dp[b].count)
        return better(left, right)
    }
}
