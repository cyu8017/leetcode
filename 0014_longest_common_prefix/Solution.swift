// LeetCode 0014 - Longest Common Prefix
// https://leetcode.com/problems/longest-common-prefix/

class Solution {
    func longestCommonPrefix(_ strs: [String]) -> String {
        if strs.isEmpty {
            return ""
        }

        let first = Array(strs[0])
        for i in first.indices {
            let ch = first[i]
            for j in 1..<strs.count {
                let chars = Array(strs[j])
                if i >= chars.count || chars[i] != ch {
                    return String(first[0..<i])
                }
            }
        }

        return strs[0]
    }
}
