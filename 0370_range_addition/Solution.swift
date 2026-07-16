// LeetCode 0370 - Range Addition
// https://leetcode.com/problems/range-addition/

class Solution {
    func getModifiedArray(_ length: Int, _ updates: [[Int]]) -> [Int] {
        var diff = Array(repeating: 0, count: length + 1)

        for update in updates {
            let start = update[0]
            let end = update[1]
            let inc = update[2]
            diff[start] += inc
            if end + 1 < diff.count {
                diff[end + 1] -= inc
            }
        }

        var result = Array(repeating: 0, count: length)
        var running = 0
        for index in 0..<length {
            running += diff[index]
            result[index] = running
        }

        return result
    }
}
