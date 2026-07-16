// LeetCode 0163 - Missing Ranges
// https://leetcode.com/problems/missing-ranges/

class Solution {
    func findMissingRanges(_ nums: [Int], _ lower: Int, _ upper: Int) -> [[Int]] {
        var result = [[Int]]()
        var previous = lower - 1
        for number in nums + [upper + 1] {
            if number - previous >= 2 { result.append([previous + 1, number - 1]) }
            previous = number
        }
        return result
    }
}