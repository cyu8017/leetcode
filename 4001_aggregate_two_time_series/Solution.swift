// LeetCode 4001 - Aggregate Two Time Series
// https://leetcode.com/problems/aggregate-two-time-series/


class Solution {
    func aggregateTimeSeries(_ series1: [[Int]], _ series2: [[Int]]) -> [[Int]] {
        let m = series1.count, n = series2.count
        var i = 0, j = 0
        var ans = [[Int]]()
        while i < m && j < n {
            let t1 = series1[i][0], v1 = series1[i][1]
            let t2 = series2[j][0], v2 = series2[j][1]
            if t1 == t2 {
                ans.append([t1, v1 + v2])
                i += 1
                j += 1
            } else if t1 < t2 {
                ans.append([t1, v1 + v2])
                i += 1
            } else {
                ans.append([t2, v1 + v2])
                j += 1
            }
        }
        while i < m {
            ans.append([series1[i][0], series1[i][1]])
            i += 1
        }
        while j < n {
            ans.append([series2[j][0], series2[j][1]])
            j += 1
        }
        return ans
    }
}
