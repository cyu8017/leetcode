// LeetCode 2649 - Nested Array Generator
// https://leetcode.com/problems/nested-array-generator/

class Solution {
    func inorderTraversal(_ arr: [Int]) -> [Int] {
        arr
    }

    func inorderTraversal(_ arr: [Any]) -> [Int] {
        var out: [Int] = []
        func dfs(_ items: [Any]) {
            for item in items {
                if let n = item as? Int {
                    out.append(n)
                } else if let nested = item as? [Any] {
                    dfs(nested)
                }
            }
        }
        dfs(arr)
        return out
    }
}
