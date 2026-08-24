// LeetCode 2700 - Differences Between Two Objects
// https://leetcode.com/problems/differences-between-two-objects/

class Solution {
    func objDiff(_ obj1: [String: Int], _ obj2: [String: Int]) -> [String: [Int]] {
        var diff: [String: [Int]] = [:]
        for (k, v1) in obj1 {
            if let v2 = obj2[k], v2 != v1 {
                diff[k] = [v1, v2]
            }
        }
        return diff
    }
}
