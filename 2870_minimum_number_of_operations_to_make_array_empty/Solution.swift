// LeetCode 2870 - Minimum Number of Operations to Make Array Empty
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        var freq: [Int: Int] = [:]
        for v in nums { freq[v, default: 0] += 1 }
        var ans = 0
        for c in freq.values {
            if c == 1 { return -1 }
            ans += (c + 2) / 3
        }
        return ans
    }
}
