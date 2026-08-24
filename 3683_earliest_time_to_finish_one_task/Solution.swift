// LeetCode 3683 - Earliest Time to Finish One Task
// https://leetcode.com/problems/earliest-time-to-finish-one-task/

class Solution {
    func earliestTime(_ tasks: [[Int]]) -> Int {
        var ans = 200
        for task in tasks { ans = min(ans, task[0] + task[1]) }
        return ans
    }
}
