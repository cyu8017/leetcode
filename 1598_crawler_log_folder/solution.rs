// LeetCode 1598 - Crawler Log Folder
// https://leetcode.com/problems/crawler-log-folder/

impl Solution {
    pub fn min_operations(logs: Vec<String>) -> i32 {
        let mut depth = 0;
        for log in logs {
            if log == "../" {
                depth = (depth - 1).max(0);
            } else if log != "./" {
                depth += 1;
            }
        }
        depth
    }
}
