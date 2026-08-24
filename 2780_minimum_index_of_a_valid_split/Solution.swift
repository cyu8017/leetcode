// LeetCode 2780 - Minimum Index of a Valid Split
// https://leetcode.com/problems/minimum-index-of-a-valid-split/

class Solution {
    func minimumIndex(_ nums: [Int]) -> Int {
        var freq: [Int: Int] = [:]
        var dom = 0, best = 0
        for v in nums {
            freq[v, default: 0] += 1
            if freq[v]! > best {
                best = freq[v]!
                dom = v
            }
        }
        var left = 0
        let n = nums.count
        for i in 0..<(n - 1) {
            if nums[i] == dom { left += 1 }
            let right = best - left
            if left * 2 > i + 1 && right * 2 > n - i - 1 { return i }
        }
        return -1
    }
}
