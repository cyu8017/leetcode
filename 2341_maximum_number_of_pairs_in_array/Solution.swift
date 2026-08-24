// LeetCode 2341 - Maximum Number of Pairs in Array
// https://leetcode.com/problems/maximum-number-of-pairs-in-array/

class Solution {
    func numberOfPairs(_ nums: [Int]) -> [Int] {
        var cnt: [Int: Int] = [:]
        for x in nums { cnt[x, default: 0] += 1 }
        var pairs = 0, left = 0
        for c in cnt.values {
            pairs += c / 2
            left += c % 2
        }
        return [pairs, left]
    }
}
