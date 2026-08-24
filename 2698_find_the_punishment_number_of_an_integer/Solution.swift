// LeetCode 2698 - Find the Punishment Number of an Integer
// https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

class Solution {
    func punishmentNumber(_ n: Int) -> Int {
        var ans = 0
        for i in 1...n {
            let sq = i * i
            if can(sq, i) { ans += sq }
        }
        return ans
    }

    private func can(_ sq: Int, _ target: Int) -> Bool {
        dfs(Array(String(sq)), 0, 0, target)
    }

    private func dfs(_ s: [Character], _ i: Int, _ sum: Int, _ target: Int) -> Bool {
        if i == s.count { return sum == target }
        var cur = 0
        for j in i..<s.count {
            cur = cur * 10 + Int(String(s[j]))!
            if sum + cur > target { break }
            if dfs(s, j + 1, sum + cur, target) { return true }
        }
        return false
    }
}
