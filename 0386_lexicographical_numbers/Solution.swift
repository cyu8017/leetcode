// LeetCode 0386 - Lexicographical Numbers
// https://leetcode.com/problems/lexicographical-numbers/

class Solution {
    func lexicalOrder(_ n: Int) -> [Int] {
        var result: [Int] = []

        func dfs(_ current: Int) {
            if current > n {
                return
            }
            result.append(current)
            dfs(current * 10)
            if current % 10 < 9 {
                dfs(current + 1)
            }
        }

        dfs(1)
        return result
    }
}
