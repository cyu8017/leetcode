// LeetCode 1655 - Distribute Repeating Integers
// https://leetcode.com/problems/distribute-repeating-integers/

class Solution {
    func canDistribute(_ nums: [Int], _ quantity: [Int]) -> Bool {
        var freq = [Int: Int]()
        for x in nums { freq[x, default: 0] += 1 }
        let cnt = Array(freq.values)
        var quantity = quantity.sorted(by: >)
        let m = quantity.count
        var sums = Array(repeating: 0, count: 1 << m)
        for mask in 1..<(1 << m) {
            let bit = mask & -mask
            let idx = bit.trailingZeroBitCount
            sums[mask] = sums[mask ^ bit] + quantity[idx]
        }
        var dp: Set<Int> = [0]
        for c in cnt {
            var nxt = dp
            for mask in dp {
                let left = ((1 << m) - 1) ^ mask
                var sub = left
                while sub > 0 {
                    if sums[sub] <= c { nxt.insert(mask | sub) }
                    sub = (sub - 1) & left
                }
            }
            dp = nxt
        }
        return dp.contains((1 << m) - 1)
    }
}
