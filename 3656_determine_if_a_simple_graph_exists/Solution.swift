// LeetCode 3656 - Determine if a Simple Graph Exists
// https://leetcode.com/problems/determine-if-a-simple-graph-exists/

class Solution {
    func simpleGraphExists(_ degrees: [Int]) -> Bool {
        let n = degrees.count
        var d = degrees.sorted(by: >)
        var sum = 0
        for x in d {
            if x < 0 || x >= n { return false }
            sum += x
        }
        if sum % 2 == 1 { return false }
        var prefix = Array(repeating: 0, count: n + 1)
        for i in 0..<n { prefix[i + 1] = prefix[i] + d[i] }
        for k in 1...n {
            var right = 0
            if k < n {
                for i in k..<n { right += d[i] < k ? d[i] : k }
            }
            if prefix[k] > k * (k - 1) + right { return false }
        }
        return true
    }
}
