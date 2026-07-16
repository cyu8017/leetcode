// LeetCode 0525 - Contiguous Array
// https://leetcode.com/problems/contiguous-array/

class Solution {
    func findMaxLength(_ nums: [Int]) -> Int {
        var counts: [Int: Int] = [0: -1]
        var balance = 0
        var best = 0
        for (index, num) in nums.enumerated() {
            balance += num == 1 ? 1 : -1
            if let previous = counts[balance] {
                best = max(best, index - previous)
            } else {
                counts[balance] = index
            }
        }
        return best
    }
}
