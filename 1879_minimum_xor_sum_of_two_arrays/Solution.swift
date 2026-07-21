// LeetCode 1879 - Minimum XOR Sum of Two Arrays
// https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution {
    func minimumXORSum(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let n = nums1.count
        let fullMask = (1 << n) - 1
        var dp = Array(repeating: Int.max, count: 1 << n)
        dp[0] = 0

        for mask in 0..<(1 << n) {
            let i = mask.nonzeroBitCount
            if i >= n {
                continue
            }
            for j in 0..<n {
                if mask & (1 << j) != 0 {
                    continue
                }
                let nextMask = mask | (1 << j)
                let cost = dp[mask] + (nums1[i] ^ nums2[j])
                if cost < dp[nextMask] {
                    dp[nextMask] = cost
                }
            }
        }

        return dp[fullMask]
    }
}
