// LeetCode 3258 - Count Substrings That Satisfy K-Constraint I
// https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/

class Solution {
    func countKConstraintSubstrings(_ s: String, _ k: Int) -> Int {
        let chars = Array(s)
        var ans = 0
        for i in 0..<chars.count {
            var z = 0, o = 0
            for j in i..<chars.count {
                if chars[j] == "0" { z += 1 } else { o += 1 }
                if z <= k || o <= k { ans += 1 }
                else { break }
            }
        }
        return ans
    }
}
