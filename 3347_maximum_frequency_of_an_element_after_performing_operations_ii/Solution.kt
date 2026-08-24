// LeetCode 3347 - Maximum Frequency of an Element After Performing Operations II
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/

class Solution {
    fun maxFrequency(nums: IntArray, k: Int, numOperations: Int): Int {
        nums.sort()
        val freq = HashMap<Int, Int>()
        for (x in nums) freq[x] = (freq[x] ?: 0) + 1
        var ans = 1
        val candidates = ArrayList<Int>()
        val seen = HashSet<Int>()
        for (x in nums) {
            for (t in intArrayOf(x - k, x, x + k)) {
                if (seen.add(t)) candidates.add(t)
            }
        }
        for (t in candidates) {
            val lo = lowerBound(nums, t - k)
            val hi = upperBound(nums, t + k)
            val can = hi - lo
            val f = freq[t] ?: 0
            val use = minOf(can, f + numOperations)
            ans = maxOf(ans, use)
        }
        return ans
    }

    private fun lowerBound(a: IntArray, x: Int): Int {
        var lo = 0
        var hi = a.size
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (a[mid] < x) lo = mid + 1 else hi = mid
        }
        return lo
    }

    private fun upperBound(a: IntArray, x: Int): Int {
        var lo = 0
        var hi = a.size
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (a[mid] <= x) lo = mid + 1 else hi = mid
        }
        return lo
    }
}
