// LeetCode 1997 - First Day Where You Have Been in All the Rooms
// https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms/

class Solution {
    func firstDayBeenInAllRooms(_ nextVisit: [Int]) -> Int {
        let MOD = 1_000_000_007
        let n = nextVisit.count
        var dp = Array(repeating: 0, count: n)
        for i in 1..<n {
            dp[i] = (2 * dp[i - 1] - dp[nextVisit[i - 1]] + 2) % MOD
            if dp[i] < 0 { dp[i] += MOD }
        }
        return dp[n - 1]
    }
}
