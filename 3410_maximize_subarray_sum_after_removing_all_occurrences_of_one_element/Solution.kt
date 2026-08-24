// LeetCode 3410 - Maximize Subarray Sum After Removing All Occurrences of One Element
// https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/

class Solution {
    private fun kadane(a: MutableList<Int>): Long {
        var best = -(1L  shl  62)
        var cur = 0
        for (x in a) {
            cur += x
            if (cur > best) best = cur
            if (cur < 0) cur = 0
        }
        var allNeg = true
        var mx = a[0]
        for (x in a) {
            if (x > mx) mx = x
            if (x >= 0) allNeg = false
        }
        if (allNeg) return mx
        return best
    }

    private fun kadane(a: IntArray): Long {
        var list = ArrayList<Int>()
        for (x in a) { list.add(x) }
        return kadane(list)
    }

    fun maxSubarraySum(nums: IntArray): Long {
        var ans = kadane(nums)
        var uniq = HashSet<Int>()
        for (x in nums) { if (x < 0) uniq.add(x) }
        for (v in uniq) {
            var b = ArrayList<Int>()
            for (x in nums) { if (x != v) b.add(x) }
            if (b.isEmpty()) continue
            var cand = kadane(b)
            if (cand > ans) ans = cand
        }
        return ans
    }
}
