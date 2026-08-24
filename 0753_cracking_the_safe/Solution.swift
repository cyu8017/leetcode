// LeetCode 0753 - Cracking the Safe
// https://leetcode.com/problems/cracking-the-safe/

class Solution {
    func crackSafe(_ n: Int, _ k: Int) -> String {
        var seen = Set<String>()
        var path = [Character]()
        let start = String(repeating: "0", count: max(0, n - 1))
        func dfs(_ node: String) {
            for d in 0..<k {
                let digit = Character(String(d))
                let edge = node + String(digit)
                if seen.insert(edge).inserted {
                    dfs(String(edge.dropFirst()))
                    path.append(digit)
                }
            }
        }
        dfs(start)
        return String(path) + start
    }
}
