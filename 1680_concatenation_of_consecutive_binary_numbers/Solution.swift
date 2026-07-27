// LeetCode 1680 - Concatenation of Consecutive Binary Numbers
// https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

class Solution {
    func concatenatedBinary(_ n: Int) -> Int {
        var ans = 0
        var bits = 0
        let mod = 1_000_000_007
        for x in 1...n {
            if x & (x - 1) == 0 { bits += 1 }
            ans = ((ans << bits) % mod + x) % mod
        }
        return ans
    }
}
