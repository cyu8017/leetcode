// LeetCode 0446 - Arithmetic Slices II - Subsequence
// https://leetcode.com/problems/arithmetic-slices-ii-subsequence/

class Solution {
    func numberOfArithmeticSlices(_ nums: [Int]) -> Int {
        var total = 0
        var differences = Array(repeating: [Int: Int](), count: nums.count)

        for index in nums.indices {
            let value = nums[index]
            for previous in 0..<index {
                let diff = value - nums[previous]
                total += differences[previous][diff, default: 0]
                differences[index][diff, default: 0] += differences[previous][diff, default: 0] + 1
            }
        }

        return total
    }
}
