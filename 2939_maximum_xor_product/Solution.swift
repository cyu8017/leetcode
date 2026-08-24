// LeetCode 2939 - Maximum Xor Product
// https://leetcode.com/problems/maximum-xor-product/

class Solution {
    func maximumXorProduct(_ a0: Int, _ b0: Int, _ n: Int) -> Int {
        let mod = 1_000_000_007
        var a = a0, b = b0
        if n > 0 {
            for i in stride(from: n - 1, through: 0, by: -1) {
                let bit = 1 << i
                let abit = a & bit, bbit = b & bit
                if abit == bbit {
                    a |= bit
                    b |= bit
                } else if a > b {
                    b |= bit
                    a &= ~bit
                } else {
                    a |= bit
                    b &= ~bit
                }
            }
        }
        return (a % mod) * (b % mod) % mod
    }
}
