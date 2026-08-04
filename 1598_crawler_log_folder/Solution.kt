// LeetCode 1598 - Crawler Log Folder
// https://leetcode.com/problems/crawler-log-folder/

class Solution {
    fun minOperations(logs: Array<String>): Int {
        var depth = 0
        for (log in logs) {
            when {
                log == "../" -> if (depth > 0) depth--
                log != "./" -> depth++
            }
        }
        return depth
    }
}
