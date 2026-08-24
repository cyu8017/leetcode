// LeetCode 2712 - Minimum Cost to Make All Characters Equal
// https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/

class Solution {
    func minimumCost(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var ans = 0
        for i in 1..<n where chars[i] != chars[i - 1] {
            ans += min(i, n - i)
        }
        return ans
    }
}
