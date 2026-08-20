// LeetCode 1450 - Number of Students Doing Homework at a Given Time
// https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

class Solution {
    func busyStudent(_ startTime: [Int], _ endTime: [Int], _ queryTime: Int) -> Int {
        zip(startTime, endTime).filter { $0 <= queryTime && queryTime <= $1 }.count
    }
}
