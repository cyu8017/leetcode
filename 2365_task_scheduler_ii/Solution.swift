// LeetCode 2365 - Task Scheduler II
// https://leetcode.com/problems/task-scheduler-ii/

class Solution {
    func taskSchedulerII(_ tasks: [Int], _ space: Int) -> Int {
        var next: [Int: Int] = [:]
        var day = 0
        for t in tasks {
            day = max(day, next[t, default: 0])
            day += 1
            next[t] = day + space
        }
        return day
    }
}
