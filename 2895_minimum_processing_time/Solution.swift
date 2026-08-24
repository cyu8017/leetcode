// LeetCode 2895 - Minimum Processing Time
// https://leetcode.com/problems/minimum-processing-time/

class Solution {
    func minProcessingTime(_ processorTime: [Int], _ tasks: [Int]) -> Int {
        let processorTime = processorTime.sorted()
        let tasks = tasks.sorted(by: >)
        var ans = 0
        for i in 0..<processorTime.count {
            ans = max(ans, processorTime[i] + tasks[i * 4])
        }
        return ans
    }
}
