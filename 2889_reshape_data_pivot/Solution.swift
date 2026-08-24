// LeetCode 2889 - Reshape Data: Pivot
// https://leetcode.com/problems/reshape-data-pivot/
// Pandas stand-in.

class Solution {
    func pivotTable(_ weather: [[Any]]) -> [[String: Any]] {
        var months: [Any] = []
        var byMonth: [String: [String: Any]] = [:]
        var monthOrder: [String] = []
        for r in weather {
            let city = "\(r[0])"
            let month = "\(r[1])"
            let temperature = r[2]
            if byMonth[month] == nil {
                byMonth[month] = [:]
                monthOrder.append(month)
            }
            byMonth[month]![city] = temperature
        }
        return monthOrder.map { month in
            var row: [String: Any] = ["month": month]
            if let cities = byMonth[month] {
                for (city, temp) in cities { row[city] = temp }
            }
            return row
        }
    }
}
