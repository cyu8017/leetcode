// LeetCode 0645 - Set Mismatch
// https://leetcode.com/problems/set-mismatch/

class Solution {
    func findErrorNums(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var seen = Array(repeating: 0, count: n + 1)
        var duplicate = -1
        var missing = -1
        for value in nums { seen[value] += 1 }
        for value in 1...n {
            if seen[value] == 2 { duplicate = value }
            else if seen[value] == 0 { missing = value }
        }
        return [duplicate, missing]
    }
}
