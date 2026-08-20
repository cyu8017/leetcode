// LeetCode 1992 - Find All Groups of Farmland
// https://leetcode.com/problems/find-all-groups-of-farmland/

class Solution {
    func findFarmland(_ land: [[Int]]) -> [[Int]] {
        let m = land.count, n = land[0].count
        var ans: [[Int]] = []
        for i in 0..<m {
            for j in 0..<n {
                if land[i][j] == 1 && (i == 0 || land[i - 1][j] == 0) && (j == 0 || land[i][j - 1] == 0) {
                    var r = i, c = j
                    while r + 1 < m && land[r + 1][j] == 1 { r += 1 }
                    while c + 1 < n && land[i][c + 1] == 1 { c += 1 }
                    ans.append([i, j, r, c])
                }
            }
        }
        return ans
    }
}
