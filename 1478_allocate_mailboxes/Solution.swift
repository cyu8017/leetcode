// LeetCode 1478 - Allocate Mailboxes
// https://leetcode.com/problems/allocate-mailboxes/

class Solution {
    func minDistance(_ houses: [Int], _ k: Int) -> Int {
        let houses = houses.sorted()
        let n = houses.count
        var cost = Array(repeating: Array(repeating: 0, count: n), count: n)
        for i in 0..<n {
            for j in i..<n {
                let mid = houses[(i + j) / 2]
                cost[i][j] = (i...j).reduce(0) { $0 + abs(houses[$1] - mid) }
            }
        }
        var dp = [0] + Array(repeating: Int.max / 4, count: n)
        for _ in 0..<k {
            var ndp = [0] + Array(repeating: Int.max / 4, count: n)
            for j in 1...n {
                ndp[j] = (0..<j).map { dp[$0] + cost[$0][j - 1] }.min()!
            }
            dp = ndp
        }
        return dp[n]
    }
}
