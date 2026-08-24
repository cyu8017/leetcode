// LeetCode 3440 - Reschedule Meetings for Maximum Free Time II
// https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/

class Solution {
    func maxFreeTime(_ eventTime: Int, _ startTime: [Int], _ endTime: [Int]) -> Int {
        let n = startTime.count
        var gaps = Array(repeating: 0, count: n + 1)
        gaps[0] = startTime[0]
        for i in 1..<n { gaps[i] = startTime[i] - endTime[i - 1] }
        gaps[n] = eventTime - endTime[n - 1]
        var ans = gaps.max() ?? 0
        var leftMax = Array(repeating: 0, count: n + 1)
        var rightMax = Array(repeating: 0, count: n + 1)
        for i in 0...n {
            leftMax[i] = gaps[i]
            if i > 0 && leftMax[i - 1] > leftMax[i] { leftMax[i] = leftMax[i - 1] }
        }
        for i in stride(from: n, through: 0, by: -1) {
            rightMax[i] = gaps[i]
            if i < n && rightMax[i + 1] > rightMax[i] { rightMax[i] = rightMax[i + 1] }
        }
        for i in 0..<n {
            let dur = endTime[i] - startTime[i]
            let merged = gaps[i] + gaps[i + 1]
            var bestOther = 0
            if i > 0 && leftMax[i - 1] > bestOther { bestOther = leftMax[i - 1] }
            if i + 2 <= n && rightMax[i + 2] > bestOther { bestOther = rightMax[i + 2] }
            var cand = merged
            if bestOther >= dur { cand = merged + dur }
            if cand > ans { ans = cand }
        }
        return ans
    }
}
