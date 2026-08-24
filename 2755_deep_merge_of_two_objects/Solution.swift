// LeetCode 2755 - Deep Merge of Two Objects
// https://leetcode.com/problems/deep-merge-of-two-objects/

class Solution {
    func deepMerge(_ obj1: [String: String], _ obj2: [String: String]) -> [String: String] {
        var output = obj1
        for (k, v) in obj2 { output[k] = v }
        return output
    }
}
