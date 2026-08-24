// LeetCode 3681 - Maximum XOR of Subsequences
// https://leetcode.com/problems/maximum-xor-of-subsequences/

class Solution {
    func maxXorSubsequences(_ nums: [Int]) -> Int {
        var basis = Array(repeating: 0, count: 32)
        for x in nums {
            var cur = x
            for b in stride(from: 31, through: 0, by: -1) {
                if (cur & (1 << b)) == 0 { continue }
                if basis[b] == 0 {
                    basis[b] = cur
                    break
                }
                cur ^= basis[b]
            }
        }
        var ans = 0
        for b in stride(from: 31, through: 0, by: -1) {
            if (ans ^ basis[b]) > ans { ans ^= basis[b] }
        }
        return ans
    }
}
