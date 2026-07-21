// LeetCode 1829 - Maximum XOR for Each Query
// https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution {
    func getMaximumXor(_ nums: [Int], _ maximumBit: Int) -> [Int] {
        let limit = (1 << maximumBit) - 1
        var current = 0
        for num in nums { current ^= num }
        var result = [Int]()
        for i in stride(from: nums.count - 1, through: 0, by: -1) {
            result.append(current ^ limit)
            current ^= nums[i]
        }
        return result
    }
}
