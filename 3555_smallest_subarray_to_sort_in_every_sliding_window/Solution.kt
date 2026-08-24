// LeetCode 3555 - Smallest Subarray to Sort in Every Sliding Window
// https://leetcode.com/problems/smallest-subarray-to-sort-in-every-sliding-window/

class Solution {
    fun minSubarraySort(nums: IntArray, k: Int): IntArray {
        val inf = 1  shl  30
        var n = nums.size
        var ans = ArrayList<Int>()
        for (i in 0..n - k) { ans.add(f(nums, i, i + k - 1, inf)) }
        return ans.stream().mapToInt(Integer::intValue).toArray()
    }

    fun f(nums: IntArray, i: Int, j: Int, inf: Int): Int {
        var mi = inf
        var mx = -inf
        var l = -1
        var r = -1
        for (p in i..j) {
            if (nums[p] < mx) r = p
            else mx = nums[p]
            var q = j - p + i
            if (nums[q] > mi) l = q
            else mi = nums[q]
        }
        if (r == -1) return 0
        return r - l + 1
    }
}
