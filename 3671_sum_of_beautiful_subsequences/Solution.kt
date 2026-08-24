// LeetCode 3671 - Sum of Beautiful Subsequences
// https://leetcode.com/problems/sum-of-beautiful-subsequences/

class Solution {
    fun totalBeauty(nums: IntArray): Int {
        val MOD = 1_000_000_007
        var mx = 0
        for (v in nums) if (v > mx) mx = v
        val pos = Array(mx + 1) { ArrayList<Int>() }
        for (i in nums.indices) pos[nums[i]].add(i)
        val cnt = IntArray(mx + 1)
        for (g in 1..mx) {
            val seq = ArrayList<Int>()
            var m = g
            while (m <= mx) {
                seq.addAll(pos[m])
                m += g
            }
            if (seq.isEmpty()) continue
            seq.sort()
            var ways = 1
            for (i in seq.indices) ways = ((ways * 2L) % MOD).toInt()
            cnt[g] = (ways - 1 + MOD) % MOD
        }
        var ans = 0
        for (g in mx downTo 1) {
            var m = 2 * g
            while (m <= mx) {
                cnt[g] = (cnt[g] - cnt[m] + MOD) % MOD
                m += g
            }
            ans = ((ans + 1L * cnt[g] * g) % MOD).toInt()
        }
        return ans
    }
}
