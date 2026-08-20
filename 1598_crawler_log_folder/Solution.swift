// LeetCode 1598 - Crawler Log Folder
// https://leetcode.com/problems/crawler-log-folder/

class Solution {
    func minOperations(_ logs: [String]) -> Int {
        var depth = 0
        for log in logs {
            if log == "../" {
                depth = max(0, depth - 1)
            } else if log != "./" {
                depth += 1
            }
        }
        return depth
    }
}
