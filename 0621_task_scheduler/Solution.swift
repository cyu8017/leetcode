// LeetCode 0621 - Task Scheduler
// https://leetcode.com/problems/task-scheduler/

class Solution {
    func leastInterval(_ tasks: [Character], _ n: Int) -> Int {
        var counts = Array(repeating: 0, count: 26)
        let a = Character("A").asciiValue!
        for task in tasks {
            counts[Int(task.asciiValue! - a)] += 1
        }
        let maxFreq = counts.max() ?? 0
        let maxCount = counts.filter { $0 == maxFreq }.count
        return max(tasks.count, (maxFreq - 1) * (n + 1) + maxCount)
    }
}
