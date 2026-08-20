// LeetCode 1573 - Number of Ways to Split a String
// https://leetcode.com/problems/number-of-ways-to-split-a-string/

class Solution {
    func numWays(_ s: String) -> Int {
        let MOD = 1_000_000_007
        let chars = Array(s)
        let ones = chars.filter { $0 == "1" }.count
        if ones % 3 != 0 { return 0 }
        if ones == 0 {
            let gaps = chars.count - 1
            return gaps * (gaps - 1) / 2 % MOD
        }
        let target = ones / 3
        var positions = [Int]()
        for (i, ch) in chars.enumerated() where ch == "1" {
            positions.append(i)
        }
        return (positions[target] - positions[target - 1]) * (positions[2 * target] - positions[2 * target - 1]) % MOD
    }
}
