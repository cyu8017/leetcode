// LeetCode 2784 - Check if Array is Good
// https://leetcode.com/problems/check-if-array-is-good/

class Solution {
    func isGood(_ nums: [Int]) -> Bool {
        let n = nums.count - 1
        if n < 1 { return false }
        var freq = Array(repeating: 0, count: n + 1)
        for v in nums {
            if v < 1 || v > n { return false }
            freq[v] += 1
        }
        for i in 1..<n where freq[i] != 1 { return false }
        return freq[n] == 2
    }
}
