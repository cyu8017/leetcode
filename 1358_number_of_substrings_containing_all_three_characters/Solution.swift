// LeetCode 1358 - Number of Substrings Containing All Three Characters
// https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

class Solution {
    func numberOfSubstrings(_ s: String) -> Int {
        var last = [-1, -1, -1], ans = 0
        for (i, c) in s.utf8.enumerated() {
            last[Int(c) - 97] = i
            ans += (last.min() ?? -1) + 1
        }
        return ans
    }
}
