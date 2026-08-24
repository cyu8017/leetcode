// LeetCode 3430 - Maximum and Minimum Sums of at Most Size K Subarrays
// https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/

class Solution {
    func minMaxSubarraySum(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var ans = 0
        for i in 0..<n {
            var mn = nums[i], mx = nums[i]
            var j = i
            while j < n && j - i + 1 <= k {
                if nums[j] < mn { mn = nums[j] }
                if nums[j] > mx { mx = nums[j] }
                ans += mn + mx
                j += 1
            }
        }
        return ans
    }
}
