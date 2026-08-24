// LeetCode 2777 - Date Range Generator
// https://leetcode.com/problems/date-range-generator/

import Foundation

class Solution {
    func dateRangeGenerator(_ start: String, _ end: String, _ step: Int) -> [String] {
        let sp = start.split(separator: "-").compactMap { Int($0) }
        let ep = end.split(separator: "-").compactMap { Int($0) }
        if sp.count != 3 || ep.count != 3 { return [] }
        var y = sp[0], m = sp[1], d = sp[2]
        let ey = ep[0], em = ep[1], ed = ep[2]
        var ans: [String] = []
        while cmp(y, m, d, ey, em, ed) {
            ans.append(String(format: "%04d-%02d-%02d", y, m, d))
            let ymd = addDays(y, m, d, step)
            y = ymd.0; m = ymd.1; d = ymd.2
        }
        return ans
    }

    private func isLeap(_ yy: Int) -> Bool {
        (yy % 4 == 0 && yy % 100 != 0) || (yy % 400 == 0)
    }

    private func addDays(_ yy0: Int, _ mm0: Int, _ dd0: Int, _ days0: Int) -> (Int, Int, Int) {
        var yy = yy0, mm = mm0, dd = dd0, days = days0
        while days > 0 {
            var mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            mdays[2] = isLeap(yy) ? 29 : 28
            dd += 1
            if dd > mdays[mm] { dd = 1; mm += 1 }
            if mm > 12 { mm = 1; yy += 1 }
            days -= 1
        }
        return (yy, mm, dd)
    }

    private func cmp(_ y: Int, _ m: Int, _ d: Int, _ ey: Int, _ em: Int, _ ed: Int) -> Bool {
        if y != ey { return y < ey }
        if m != em { return m < em }
        return d <= ed
    }
}
