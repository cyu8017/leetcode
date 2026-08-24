// LeetCode 0568 - Maximum Vacation Days
// https://leetcode.com/problems/maximum-vacation-days/

class Solution {
    func maxVacationDays(_ flights: [[Int]], _ days: [[Int]]) -> Int {
        let cities = flights.count
        let weeks = days[0].count
        let NEG = -1_000_000_000
        var dp = Array(repeating: NEG, count: cities)
        dp[0] = 0
        for week in 0..<weeks {
            var nxt = Array(repeating: NEG, count: cities)
            for city in 0..<cities where dp[city] != NEG {
                for dest in 0..<cities {
                    if dest == city || flights[city][dest] == 1 {
                        nxt[dest] = max(nxt[dest], dp[city] + days[dest][week])
                    }
                }
            }
            dp = nxt
        }
        return dp.max() ?? 0
    }
}
