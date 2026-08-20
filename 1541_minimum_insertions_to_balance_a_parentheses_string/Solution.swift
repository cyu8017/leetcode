// LeetCode 1541 - Minimum Insertions to Balance a Parentheses String
// https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/

class Solution {
    func minInsertions(_ s: String) -> Int {
        var insertions = 0, needed = 0
        for ch in s {
            if ch == "(" {
                needed += 2
                if needed & 1 != 0 {
                    insertions += 1
                    needed -= 1
                }
            } else {
                needed -= 1
                if needed < 0 {
                    insertions += 1
                    needed = 1
                }
            }
        }
        return insertions + needed
    }
}
