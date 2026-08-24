// LeetCode 3439 - Reschedule Meetings for Maximum Free Time I
// https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/

class Solution {
    func maxFreeTime(_ eventTime: Int, _ k: Int, _ startTime: [Int], _ endTime: [Int]) -> Int {
        let n = startTime.count
        var gaps = Array(repeating: 0, count: n + 1)
        gaps[0] = startTime[0]
        for i in 1..<n { gaps[i] = startTime[i] - endTime[i - 1] }
        gaps[n] = eventTime - endTime[n - 1]
        let window = k + 1
        var sum = 0
        for i in 0..<min(window, gaps.count) { sum += gaps[i] }
        var ans = sum
        if window < gaps.count {
            for i in window..<gaps.count {
                sum += gaps[i] - gaps[i - window]
                if sum > ans { ans = sum }
            }
        }
        return ans
    }
}
