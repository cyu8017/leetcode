// LeetCode 2382 - Maximum Segment Sum After Removals
// https://leetcode.com/problems/maximum-segment-sum-after-removals/

class Solution {
    private lateinit var parent: IntArray
    private lateinit var sum: LongArray
    private lateinit var active: BooleanArray

    fun maximumSegmentSum(nums: IntArray, removeQueries: IntArray): LongArray {
        val n = nums.size
        parent = IntArray(n) { it }
        sum = LongArray(n)
        active = BooleanArray(n)
        val ans = LongArray(n)
        var best = 0L
        for (i in n - 1 downTo 0) {
            ans[i] = best
            val idx = removeQueries[i]
            active[idx] = true
            sum[idx] = nums[idx].toLong()
            if (idx > 0 && active[idx - 1]) unite(idx, idx - 1)
            if (idx + 1 < n && active[idx + 1]) unite(idx, idx + 1)
            best = maxOf(best, sum[find(idx)])
        }
        return ans
    }

    private fun find(x: Int): Int {
        if (parent[x] != x) parent[x] = find(parent[x])
        return parent[x]
    }

    private fun unite(a: Int, b: Int) {
        val ra = find(a)
        val rb = find(b)
        if (ra == rb) return
        parent[rb] = ra
        sum[ra] += sum[rb]
    }
}
