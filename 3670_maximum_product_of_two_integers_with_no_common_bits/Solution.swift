// LeetCode 3670 - Maximum Product of Two Integers With No Common Bits
// https://leetcode.com/problems/maximum-product-of-two-integers-with-no-common-bits/

class Solution {
    func maxProduct(_ nums: [Int]) -> Int {
        var maxV = 0
        for v in nums { maxV = max(maxV, v) }
        var bitsN = 0
        var x = maxV
        while x > 0 { bitsN += 1; x >>= 1 }
        if bitsN == 0 { bitsN = 1 }
        let size = 1 << bitsN
        var best = Array(repeating: 0, count: size)
        for v in nums where v > best[v] { best[v] = v }
        for mask in 0..<size {
            for b in 0..<bitsN {
                if (mask & (1 << b)) != 0 {
                    let sub = mask ^ (1 << b)
                    if best[sub] > best[mask] { best[mask] = best[sub] }
                }
            }
        }
        var ans = 0
        for v in nums {
            let comp = (size - 1) ^ v
            if best[comp] > 0 { ans = max(ans, v * best[comp]) }
        }
        return ans
    }
}
