// LeetCode 3312 - Sorted GCD Pair Queries
// https://leetcode.com/problems/sorted-gcd-pair-queries/

class Solution {
    fun gcdValues(nums: IntArray, queries: LongArray): IntArray {
        var maxV = 0
        for (x in nums) { if (x > maxV) maxV = x }
        var cnt = IntArray(maxV + 1)
        for (x in nums) { cnt[x] = cnt[x] + 1 }
        var divCnt = LongArray(maxV + 1)
        for (g in 1 ..maxV) {
            var c = 0
            run {
                var m = g
                while (m <= maxV) {
                    c += cnt[m]
                    m += g
                }
            }
            divCnt[g] = c * (c - 1) / 2
        }
        var exact = LongArray(maxV + 1)
        for (g in maxV downTo 1) {
            exact[g] = divCnt[g]
            run {
                var m = 2 * g
                while (m <= maxV) {
                    exact[g] -= exact[m]
                    m += g
                }
            }
        }
        var pref = LongArray(maxV + 1)
        for (g in 1 ..maxV) { pref[g] = pref[g - 1] + exact[g] }
        var ans = IntArray(queries.size)
        for (i in 0 until queries.size) {
            var q = queries[i]
            var lo = 1
            var hi = maxV
            while (lo < hi) {
                var mid = (lo + hi) / 2
                if (pref[mid] > q) hi = mid
                else lo = mid + 1
            }
            ans[i] = lo
        }
        return ans
    }
}
