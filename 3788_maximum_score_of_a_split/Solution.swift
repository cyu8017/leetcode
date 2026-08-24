// LeetCode 3788 - Maximum Score Of A Split
// https://leetcode.com/problems/maximum-score-of-a-split/

class Solution {
    func maximumScore(_ nums: [Int]) -> Int {
        let n = nums.count
        var suf = [Int](repeating: 0, count: n)
        suf[n - 1] = nums[n - 1]
        if n >= 2 {
            for i in stride(from: n - 2, through: 0, by: -1) {
                suf[i] = min(nums[i], suf[i + 1])
            }
        }
        var pre = 0
        var ans = Int.min
        for i in 0..<(n - 1) {
            pre += nums[i]
            ans = max(ans, pre - suf[i + 1])
        }
        return ans
    }
}
