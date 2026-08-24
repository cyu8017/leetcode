// LeetCode 3757 - Number of Effective Subsequences
// https://leetcode.com/problems/number-of-effective-subsequences/

class Solution {
    private func popCount(_ x: Int) -> Int {
        var x = x, c = 0
        while x != 0 { c += x & 1; x >>= 1 }
        return c
    }

    func countEffectiveSubsequences(_ nums: [Int]) -> Int {
        let mod = 1_000_000_007
        var all = 0
        for x in nums { all |= x }
        var bits = [Int]()
        for b in 0..<20 where ((all >> b) & 1) != 0 { bits.append(b) }
        let m = bits.count
        var freq = [Int](repeating: 0, count: 1 << m)
        for x in nums {
            var mask = 0
            for i in 0..<m where ((x >> bits[i]) & 1) != 0 { mask |= 1 << i }
            freq[mask] += 1
        }
        var disjoint = freq
        for b in 0..<m {
            for mask in 0..<(1 << m) {
                if ((mask >> b) & 1) != 0 { disjoint[mask] += disjoint[mask ^ (1 << b)] }
            }
        }
        var pow2 = [Int](repeating: 0, count: nums.count + 1)
        pow2[0] = 1
        if nums.count >= 1 {
            for i in 1...nums.count { pow2[i] = pow2[i - 1] * 2 % mod }
        }
        var ans = 0
        let full = (1 << m) - 1
        if full >= 1 {
            for s in 1...full {
                let ways = pow2[disjoint[full ^ s]]
                let bc = popCount(s)
                if (bc & 1) != 0 {
                    ans += ways
                    if ans >= mod { ans -= mod }
                } else {
                    ans -= ways
                    if ans < 0 { ans += mod }
                }
            }
        }
        return ans
    }
}
