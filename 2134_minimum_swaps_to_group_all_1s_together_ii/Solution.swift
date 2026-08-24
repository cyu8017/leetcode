// LeetCode 2134 - Minimum Swaps to Group All 1's Together II
// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

class Solution {
    func minSwaps(_ nums: [Int]) -> Int {
        let ones = nums.reduce(0, +)
        if ones == 0 { return 0 }
        let n = nums.count
        var window = nums[0..<ones].reduce(0, +)
        var best = window
        for i in 0..<n {
            window -= nums[i]
            window += nums[(i + ones) % n]
            best = max(best, window)
        }
        return ones - best
    }
}
