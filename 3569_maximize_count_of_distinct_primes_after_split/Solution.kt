// LeetCode 3569 - Maximize Count of Distinct Primes After Split
// https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/

class Solution {
    fun maximumCount(nums: IntArray, queries: Array<IntArray>): IntArray {
        var mx = 0
        for (v in nums) { mx = maxOf(mx, v) }
        for (q in queries) { mx = maxOf(mx, q[1]) }
        var isP = BooleanArray(mx + 1)
        for (i in 2..mx) { isP[i] = true }
        var i = 2
        while (i * i <= mx) {
            if (isP[i]) var j: Int = i * i
while (j <= mx) {
isP[j] = false
            i = i + 1
        }
        var ans = IntArray(queries.size)
        for (qi in 0 until queries.size) {
            nums[queries[qi][0]] = queries[qi][1]
            var best = 0
            var left = HashMap<Int, Int>()
            var right = HashMap<Int, Int>()
            for (v in nums) { if (v <= mx && isP[v]) right.merge(v, 1, Integer::sum) }
            for (i in 0 until nums.size - 1) {
                var v = nums[i]
                if (v <= mx && isP[v]) {
                    left.merge(v, 1, Integer::sum)
                    var c = right[v] - 1
                    if (c == 0) right.remove(v)
                    else right[v] = c
                }
                best = maxOf(best, left.size + right.size)
            }
            ans[qi] = best
        }
        return ans
    }
}
j += i
}
