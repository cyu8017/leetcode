// LeetCode 1395 - Count Number of Teams
// https://leetcode.com/problems/count-number-of-teams/

class Solution {
    func numTeams(_ rating: [Int]) -> Int {
        var ans = 0
        for j in 0..<rating.count {
            let x = rating[j]
            let ll = rating[..<j].filter { $0 < x }.count
            let lg = j - ll
            let rg = rating[(j + 1)...].filter { $0 > x }.count
            let rl = rating.count - j - 1 - rg
            ans += ll * rg + lg * rl
        }
        return ans
    }
}
