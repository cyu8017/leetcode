// LeetCode 2450 - Number of Distinct Binary Strings After Applying Operations
// https://leetcode.com/problems/number-of-distinct-binary-strings-after-applying-operations/

class Solution {
    func countDistinctStrings(_ s: String, _ k: Int) -> Int {
        let mod = 1_000_000_007
        let n = s.count
        var ans = 1
        if n - k + 1 > 0 {
            for _ in 0..<(n - k + 1) {
                ans = ans * 2 % mod
            }
        }
        return ans
    }
}
