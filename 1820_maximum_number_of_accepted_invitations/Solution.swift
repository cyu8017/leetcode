// LeetCode 1820 - Maximum Number of Accepted Invitations
// https://leetcode.com/problems/maximum-number-of-accepted-invitations/

class Solution {
    func maximumInvitations(_ grid: [[Int]]) -> Int {
        let boys = grid.count
        let girls = grid[0].count
        var matchGirl = Array(repeating: -1, count: girls)

        func dfs(_ boy: Int, _ seen: inout [Bool]) -> Bool {
            for girl in 0..<girls where grid[boy][girl] == 1 && !seen[girl] {
                seen[girl] = true
                if matchGirl[girl] == -1 || dfs(matchGirl[girl], &seen) {
                    matchGirl[girl] = boy
                    return true
                }
            }
            return false
        }

        var ans = 0
        for boy in 0..<boys {
            var seen = Array(repeating: false, count: girls)
            if dfs(boy, &seen) { ans += 1 }
        }
        return ans
    }
}
