// LeetCode 2598 - Smallest Missing Non-negative Integer After Operations
// https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/

class Solution {
    func findSmallestInteger(_ nums: [Int], _ value: Int) -> Int {
        var cnt = [Int](repeating: 0, count: value)
        for x in nums {
            var r = x % value
            if r < 0 { r += value }
            cnt[r] += 1
        }
        var mex = 0
        while cnt[mex % value] > 0 {
            cnt[mex % value] -= 1
            mex += 1
        }
        return mex
    }
}
