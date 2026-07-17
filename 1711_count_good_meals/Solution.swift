// LeetCode 1711 - Count Good Meals
// https://leetcode.com/problems/count-good-meals/

class Solution {
    func countPairs(_ deliciousness: [Int]) -> Int {
        let mod = 1_000_000_007
        var seen = [Int: Int]()
        var ans = 0
        for value in deliciousness {
            for power in 0..<22 {
                if let count = seen[(1 << power) - value] {
                    ans += count
                }
            }
            seen[value, default: 0] += 1
        }
        return ans % mod
    }
}
