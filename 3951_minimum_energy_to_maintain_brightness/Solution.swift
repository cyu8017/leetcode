// LeetCode 3951 - Minimum Energy to Maintain Brightness
// https://leetcode.com/problems/minimum-energy-to-maintain-brightness/


class Solution {
    func minEnergy(_ n: Int, _ brightness: Int, _ intervals: [[Int]]) -> Int {
        var intervals = intervals.sorted { $0[0] < $1[0] }
        var merged = [[intervals[0][0], intervals[0][1]]]
        for i in 1..<intervals.count {
            let x = intervals[i]
            if merged[merged.count - 1][1] < x[0] {
                merged.append([x[0], x[1]])
            } else if x[1] > merged[merged.count - 1][1] {
                merged[merged.count - 1][1] = x[1]
            }
        }
        var ans = 0
        for interval in merged {
            let m = interval[1] - interval[0] + 1
            ans += ((brightness + 2) / 3) * m
        }
        return ans
    }
}
