// LeetCode 1154 - Day of the Year
// https://leetcode.com/problems/day-of-the-year/

class Solution {
    func dayOfYear(_ date: String) -> Int {
        let parts = date.split(separator: "-").map { Int($0)! }
        let year = parts[0], month = parts[1], day = parts[2]
        let leap = year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)
        let days = [31, leap ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return days.prefix(month - 1).reduce(0, +) + day
    }
}
