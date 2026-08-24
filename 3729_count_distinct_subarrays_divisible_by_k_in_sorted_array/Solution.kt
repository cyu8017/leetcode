// LeetCode 3729 - Count Distinct Subarrays Divisible By K In Sorted Array
// https://leetcode.com/problems/count_distinct_subarrays_divisible_by_k_in_sorted_array/

class Solution {
    fun numGoodSubarrays(nums: IntArray, k: Int): Long {
        var ans = 0
        var s = 0
        var cnt = HashMap<Int, Int>()
        cnt[0] = 1
        for (x in nums) {
            s = (s + x) % k
            ans += cnt.getOrDefault(s, 0)
            cnt[s] = cnt.getOrDefault(s, 0) + 1
        }
        var n = nums.size
        var i = 0
        while (i < n) {
            var j = i + 1
            while (j < n && nums[j] == nums[i]) { j += 1 }
            var m = j - i
            for (h in 1 ..m) {
                if (1L * nums[i] * h % k == 0) ans -= (m - h)
            }
            i = j
            
        }
        return ans
    }
}
