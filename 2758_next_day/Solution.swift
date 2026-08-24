// LeetCode 2758 - Next Day
// https://leetcode.com/problems/next-day/

import Foundation

class Solution {
    func nextDay(_ date: String) -> String {
        let parts = date.split(separator: "-").map { Int($0)! }
        if parts.count != 3 { return date }
        var y = parts[0], m = parts[1], d = parts[2]
        var mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if isLeap(y) { mdays[2] = 29 }
        d += 1
        if d > mdays[m] { d = 1; m += 1 }
        if m > 12 { m = 1; y += 1 }
        return String(format: "%04d-%02d-%02d", y, m, d)
    }

    private func isLeap(_ yy: Int) -> Bool {
        (yy % 4 == 0 && yy % 100 != 0) || (yy % 400 == 0)
    }
}
