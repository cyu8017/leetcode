// LeetCode 1575 - Count All Possible Routes
// https://leetcode.com/problems/count-all-possible-routes/

class Solution {
    func countRoutes(_ locations: [Int], _ start: Int, _ finish: Int, _ fuel: Int) -> Int {
        let MOD = 1_000_000_007
        var memo = [Int: Int]()
        func dp(_ city: Int, _ left: Int) -> Int {
            let key = city * 1000 + left
            if let v = memo[key] { return v }
            var total = city == finish ? 1 : 0
            for nxt in 0..<locations.count {
                let cost = abs(locations[city] - locations[nxt])
                if nxt != city && cost <= left {
                    total = (total + dp(nxt, left - cost)) % MOD
                }
            }
            memo[key] = total
            return total
        }
        return dp(start, fuel)
    }
}
