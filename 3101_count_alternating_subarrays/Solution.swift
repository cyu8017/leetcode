// LeetCode 3101 - Count Alternating Subarrays
// https://leetcode.com/problems/count-alternating-subarrays/

class Solution {
    func countAlternatingSubarrays(_ nums: [Int]) -> Int {
        var ans = 1, s = 1
        for i in 1..<nums.count {
            s = nums[i] != nums[i - 1] ? s + 1 : 1
            ans += s
        }
        return ans
    }
}
