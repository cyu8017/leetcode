// LeetCode 2147 - Number of Ways to Divide a Long Corridor
// https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/

class Solution {
    func numberOfWays(_ corridor: String) -> Int {
        let MOD = 1_000_000_007
        var seats = [Int]()
        for (i, c) in corridor.enumerated() where c == "S" { seats.append(i) }
        if seats.isEmpty || seats.count % 2 != 0 { return 0 }
        var ans = 1
        var i = 2
        while i < seats.count {
            ans = ans * (seats[i] - seats[i - 1]) % MOD
            i += 2
        }
        return ans
    }
}
