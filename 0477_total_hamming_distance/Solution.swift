// LeetCode 0477 - Total Hamming Distance
// https://leetcode.com/problems/total-hamming-distance/

class Solution {
    func totalHammingDistance(_ nums: [Int]) -> Int {
        var total = 0
        for bit in 0..<32 {
            var zeros = 0
            var ones = 0
            for value in nums {
                if value & (1 << bit) != 0 {
                    ones += 1
                } else {
                    zeros += 1
                }
            }
            total += zeros * ones
        }
        return total
    }
}
