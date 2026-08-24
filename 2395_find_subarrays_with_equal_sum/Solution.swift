// LeetCode 2395 - Find Subarrays With Equal Sum
// https://leetcode.com/problems/find-subarrays-with-equal-sum/

class Solution {
    func findSubarrays(_ nums: [Int]) -> Bool {
        var seen = Set<Int>()
        if nums.count >= 2 {
            for i in 0..<(nums.count - 1) {
                let s = nums[i] + nums[i + 1]
                if seen.contains(s) { return true }
                seen.insert(s)
            }
        }
        return false
    }
}
