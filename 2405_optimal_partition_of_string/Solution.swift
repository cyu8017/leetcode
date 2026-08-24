// LeetCode 2405 - Optimal Partition of String
// https://leetcode.com/problems/optimal-partition-of-string/

class Solution {
    func partitionString(_ s: String) -> Int {
        var ans = 1, seen = 0
        for c in s.utf8 {
            let bit = 1 << Int(c - 97)
            if (seen & bit) != 0 {
                ans += 1
                seen = 0
            }
            seen |= bit
        }
        return ans
    }
}
