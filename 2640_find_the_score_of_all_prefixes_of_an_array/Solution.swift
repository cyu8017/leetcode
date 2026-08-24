// LeetCode 2640 - Find the Score of All Prefixes of an Array
// https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/

class Solution {
    func findPrefixScore(_ nums: [Int]) -> [Int] {
        var ans = Array(repeating: 0, count: nums.count)
        var mx = 0
        var sum = 0
        for i in nums.indices {
            mx = max(mx, nums[i])
            sum += nums[i] + mx
            ans[i] = sum
        }
        return ans
    }
}
