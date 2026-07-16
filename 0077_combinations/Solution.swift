// LeetCode 0077 - Combinations
// https://leetcode.com/problems/combinations/

class Solution {
    func combine(_ n: Int, _ k: Int) -> [[Int]] {
        var result: [[Int]] = []
        var path: [Int] = []

        func backtrack(_ start: Int) {
            if path.count == k {
                result.append(path)
                return
            }

            let remaining = k - path.count
            for i in start...(n - remaining + 1) {
                path.append(i)
                backtrack(i + 1)
                path.removeLast()
            }
        }

        backtrack(1)
        return result
    }
}
