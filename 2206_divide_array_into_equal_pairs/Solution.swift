// LeetCode 2206 - Divide Array Into Equal Pairs
// https://leetcode.com/problems/divide-array-into-equal-pairs/

class Solution {
    func divideArray(_ nums: [Int]) -> Bool {
        var freq: [Int: Int] = [:]
        for x in nums { freq[x, default: 0] += 1 }
        return freq.values.allSatisfy { $0 % 2 == 0 }
    }
}
