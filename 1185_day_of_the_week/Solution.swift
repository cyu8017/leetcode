// LeetCode 1185 - Day of the Week
// https://leetcode.com/problems/day-of-the-week/

class Solution {
    func dayOfTheWeek(_ day: Int, _ month: Int, _ year: Int) -> String {
        let names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        var y = year, m = month, d = day
        if m < 3 { m += 12; y -= 1 }
        let c = y / 100
        y %= 100
        let w = (d + 13 * (m + 1) / 5 + y + y / 4 + c / 4 + 5 * c) % 7
        return names[(w + 6) % 7]
    }
}
