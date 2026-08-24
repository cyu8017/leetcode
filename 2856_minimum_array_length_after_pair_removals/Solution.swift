// LeetCode 2856 - Minimum Array Length After Pair Removals
// https://leetcode.com/problems/minimum-array-length-after-pair-removals/

class Solution {
    func minLengthAfterRemovals(_ nums: [Int]) -> Int {
        let n = nums.count
        var freq: [Int: Int] = [:]
        var mx = 0
        for v in nums {
            freq[v, default: 0] += 1
            mx = max(mx, freq[v]!)
        }
        if mx <= n / 2 { return n % 2 }
        return 2 * mx - n
    }
}
