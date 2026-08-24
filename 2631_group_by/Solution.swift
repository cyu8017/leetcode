// LeetCode 2631 - Group By
// https://leetcode.com/problems/group-by/

class Solution {
    func groupBy(_ arr: [Int], _ fn: (Int) -> String) -> [String: [Int]] {
        var out: [String: [Int]] = [:]
        for x in arr {
            out[fn(x), default: []].append(x)
        }
        return out
    }
}
