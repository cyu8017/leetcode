// LeetCode 2875 - Minimum Size Subarray in Infinite Array
// https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/


class Solution {
    fun minSizeSubarray(nums: IntArray, target: Int): Int {
        val n = nums.size
        var total = 0L
        for (v in nums) total += v
        var ans = 1 shl 30
        if (total > 0) {
            val loops = (target / total).toInt()
            val remain = (target % total).toInt()
            if (remain == 0) return loops * n
            val arr = IntArray(2 * n)
            nums.copyInto(arr, 0, 0, n)
            nums.copyInto(arr, n, 0, n)
            var left = 0
            var sum = 0
            var best = 1 shl 30
            for (right in arr.indices) {
                sum += arr[right]
                while (sum > remain && left <= right) {
                    sum -= arr[left]
                    left++
                }
                if (sum == remain && right - left + 1 < best) best = right - left + 1
            }
            if (best < (1 shl 30)) ans = loops * n + best
        }
        return if (ans == (1 shl 30)) -1 else ans
    }
}
