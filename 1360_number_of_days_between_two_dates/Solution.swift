// LeetCode 1360 - Number of Days Between Two Dates
// https://leetcode.com/problems/number-of-days-between-two-dates/

class Solution {
    func daysBetweenDates(_ date1: String, _ date2: String) -> Int {
        func days(_ s: String) -> Int {
            let p = s.split(separator: "-").map { Int($0)! }
            let y = p[0], m = p[1], d = p[2]
            let mdays = [0,31,28,31,30,31,30,31,31,30,31,30,31]
            func leap(_ y: Int) -> Bool { y % 400 == 0 || (y % 4 == 0 && y % 100 != 0) }
            var total = d
            for year in 1971..<y { total += leap(year) ? 366 : 365 }
            for month in 1..<m {
                total += mdays[month]
                if month == 2 && leap(y) { total += 1 }
            }
            return total
        }
        return abs(days(date1) - days(date2))
    }
}
