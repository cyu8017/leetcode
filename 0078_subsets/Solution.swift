// LeetCode 0078 - Subsets
// https://leetcode.com/problems/subsets/

class Solution {
    func subsets(_ nums: [Int]) -> [[Int]] {
        var result: [[Int]] = [[]]

        for num in nums {
            let size = result.count
            for i in 0..<size {
                result.append(result[i] + [num])
            }
        }

        return result
    }
}
