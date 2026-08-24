// LeetCode 2822 - Inversion of Object
// https://leetcode.com/problems/inversion-of-object/

class Solution {
    func invertObject(_ obj: [String: String]) -> [String: [String]] {
        var output: [String: [String]] = [:]
        for (k, v) in obj { output[v, default: []].append(k) }
        return output
    }
}
