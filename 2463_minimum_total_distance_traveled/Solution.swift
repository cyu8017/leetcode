// LeetCode 2463 - Minimum Total Distance Traveled
// https://leetcode.com/problems/minimum-total-distance-traveled/

class Solution {
    func minimumTotalDistance(_ robot: [Int], _ factory: [[Int]]) -> Int {
        let robots = robot.sorted()
        let factory = factory.sorted { $0[0] < $1[0] }
        let m = robots.count
        var pos = [Int]()
        for f in factory {
            for _ in 0..<f[1] { pos.append(f[0]) }
        }
        let n = pos.count
        let INF = Int.max / 4
        var dp = [[Int]](repeating: [Int](repeating: INF, count: n + 1), count: m + 1)
        for j in 0...n { dp[0][j] = 0 }
        if m == 0 { return 0 }
        for i in 1...m {
            if i > n { break }
            for j in i...n {
                dp[i][j] = dp[i][j - 1]
                let cost = dp[i - 1][j - 1] + abs(robots[i - 1] - pos[j - 1])
                if cost < dp[i][j] { dp[i][j] = cost }
            }
        }
        return dp[m][n]
    }
}
