// LeetCode 1411 - Number of Ways to Paint N × 3 Grid
// https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/

class Solution {
    func numOfWays(_ n: Int) -> Int {
        let mod = 1_000_000_007
        var aba = 6, abc = 6
        if n == 1 { return 12 }
        for _ in 1..<n {
            let nAba = (3 * aba + 2 * abc) % mod
            let nAbc = (2 * aba + 2 * abc) % mod
            aba = nAba; abc = nAbc
        }
        return (aba + abc) % mod
    }
}
