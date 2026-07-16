// LeetCode 0062 - Unique Paths
// https://leetcode.com/problems/unique-paths/

class Solution {
    func uniquePaths(_ m: Int, _ n: Int) -> Int {
        var row = Array(repeating: 1, count: n)

        if m > 1 {
            for _ in 1..<m {
                for col in 1..<n {
                    row[col] += row[col - 1]
                }
            }
        }

        return row[n - 1]
    }
}
