// LeetCode 2104 - Sum of Subarray Ranges
// https://leetcode.com/problems/sum-of-subarray-ranges/

class Solution {
    func subArrayRanges(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = 0
        for i in 0..<n {
            var mn = nums[i], mx = nums[i]
            for j in i..<n {
                mn = min(mn, nums[j])
                mx = max(mx, nums[j])
                ans += mx - mn
            }
        }
        return ans
    }
}
