// LeetCode 2432 - The Employee That Worked on the Longest Task
// https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/

class Solution {
    func hardestWorker(_ n: Int, _ logs: [[Int]]) -> Int {
        var ans = logs[0][0], best = logs[0][1], prev = 0
        for log in logs {
            let dur = log[1] - prev
            if dur > best || (dur == best && log[0] < ans) {
                best = dur
                ans = log[0]
            }
            prev = log[1]
        }
        return ans
    }
}
