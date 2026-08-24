// LeetCode 3630 - Partition Array for Maximum XOR and AND
// https://leetcode.com/problems/partition-array-for-maximum-xor-and-and/

class Solution {
    func maximizeXorAndXor(_ nums: [Int]) -> Int {
        let n = nums.count
        var best = 0
        for mask in 0..<(1 << n) {
            var andVal = -1, xorRest = 0
            for i in 0..<n {
                if ((mask >> i) & 1) != 0 {
                    andVal = andVal < 0 ? nums[i] : (andVal & nums[i])
                } else {
                    xorRest ^= nums[i]
                }
            }
            if andVal < 0 { andVal = 0 }
            let comp = ((1 << n) - 1) ^ mask
            var sub = comp
            while true {
                var x1 = 0
                for i in 0..<n where ((sub >> i) & 1) != 0 { x1 ^= nums[i] }
                let x2 = xorRest ^ x1
                best = max(best, andVal + x1 + x2)
                if sub == 0 { break }
                sub = (sub - 1) & comp
            }
        }
        return best
    }
}
