// LeetCode 3434 - Maximum Frequency After Subarray Operation
// https://leetcode.com/problems/maximum-frequency-after-subarray-operation/

class Solution {
    fun maxFrequency(nums: IntArray, k: Int): Int {
        var base = 0
        for (x in nums) { if (x == k) base++ }
        var ans = base
        var uniq = HashSet<Int>()
        for (x in nums) { uniq.add(x) }
        for (v in uniq) {
            if (v == k) continue
            var best = 0
            var cur = 0
            for (x in nums) {
                var delta = 0
                if (x == v) delta = 1
                else if (x == k) delta = -1
                cur += delta
                if (cur < 0) cur = 0
                if (cur > best) best = cur
            }
            if (base + best > ans) ans = base + best
        }
        return ans
    }
}
