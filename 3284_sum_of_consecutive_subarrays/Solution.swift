// LeetCode 3284 - Sum of Consecutive Subarrays
// https://leetcode.com/problems/sum-of-consecutive-subarrays/

class Solution {
    func rangeSum(_ nums: [Int]) -> Int {
        let mod = 1_000_000_007
        let n = nums.count
        var ans = 0, i = 0
        while i < n {
            var j = i
            while j + 1 < n && (nums[j + 1] == nums[j] + 1 || nums[j + 1] == nums[j] - 1) { j += 1 }
            for L in i...j {
                var s = 0
                for R in L...j {
                    s += nums[R]
                    ans = (ans + s) % mod
                }
            }
            i = j + 1
        }
        return ans
    }
}
