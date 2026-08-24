// LeetCode 2465 - Number of Distinct Averages
// https://leetcode.com/problems/number-of-distinct-averages/

class Solution {
    func distinctAverages(_ nums: [Int]) -> Int {
        let nums = nums.sorted()
        var seen = Set<Int>()
        var l = 0, r = nums.count - 1
        while l < r {
            seen.insert(nums[l] + nums[r])
            l += 1
            r -= 1
        }
        return seen.count
    }
}
