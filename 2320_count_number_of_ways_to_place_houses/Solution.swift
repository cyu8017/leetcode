// LeetCode 2320 - Count Number of Ways to Place Houses
// https://leetcode.com/problems/count-number-of-ways-to-place-houses/

class Solution {
    func countHousePlacements(_ n: Int) -> Int {
        let mod = 1_000_000_007
        var a = 1, b = 1
        for _ in 1...n {
            let na = (a + b) % mod
            b = a
            a = na
        }
        let ways = (a + b) % mod
        return ways * ways % mod
    }
}
