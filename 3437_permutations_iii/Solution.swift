// LeetCode 3437 - Permutations III
// https://leetcode.com/problems/permutations-iii/

class Solution {
    func permute(_ n: Int) -> [[Int]] {
        var ans = [[Int]]()
        var used = Array(repeating: false, count: n + 1)
        var cur = [Int]()
        func dfs() {
            if cur.count == n {
                ans.append(cur)
                return
            }
            for i in 1...n {
                if used[i] { continue }
                if !cur.isEmpty && (cur.last! % 2 == i % 2) { continue }
                used[i] = true
                cur.append(i)
                dfs()
                cur.removeLast()
                used[i] = false
            }
        }
        dfs()
        return ans
    }
}
