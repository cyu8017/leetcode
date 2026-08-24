// LeetCode 3019 - Number of Changing Keys
// https://leetcode.com/problems/number-of-changing-keys/

class Solution {
    func countKeyChanges(_ s: String) -> Int {
        let s = s.lowercased()
        let chars = Array(s)
        var ans = 0
        for i in 1..<chars.count where chars[i] != chars[i - 1] {
            ans += 1
        }
        return ans
    }
}
