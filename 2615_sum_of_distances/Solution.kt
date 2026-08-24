// LeetCode 2615 - Sum of Distances
// https://leetcode.com/problems/sum-of-distances/

class Solution {
    fun distance(nums: IntArray): LongArray {
        var n = nums.size
        var ans = LongArray(n)
        var pos = HashMap<Int, MutableList<Int>>()
        for (i in 0 until n) {
            pos.getOrPut(nums[i]) { ArrayList() }.add(i)
        }
        for (idxs in pos.values) {
            var m = idxs.size
            var pref = LongArray(m + 1)
            for (i in 0 until m) { pref[i + 1] = pref[i] + idxs[i] }
            for (j in 0 until m) {
                var idx = idxs[j]
                var left = j * idx - pref[j]
                var right = pref[m] - pref[j + 1] - (m - 1 - j) * idx
                ans[idx] = left + right
            }
        }
        return ans
    }
}
