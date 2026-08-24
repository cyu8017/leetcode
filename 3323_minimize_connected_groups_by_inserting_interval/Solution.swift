// LeetCode 3323 - Minimize Connected Groups by Inserting Interval
// https://leetcode.com/problems/minimize-connected-groups-by-inserting-interval/

class Solution {
    func minConnectedGroups(_ intervals: [[Int]], _ k: Int) -> Int {
        let intervals = intervals.sorted { $0[0] < $1[0] }
        var merged = [[Int]]()
        for it in intervals {
            if merged.isEmpty || it[0] > merged[merged.count - 1][1] {
                merged.append(it)
            } else if it[1] > merged[merged.count - 1][1] {
                merged[merged.count - 1][1] = it[1]
            }
        }
        let m = merged.count
        var ans = m
        for i in 0..<m {
            let end = merged[i][1] + k
            var j = i
            while j < m && merged[j][0] <= end { j += 1 }
            let groups = i + 1 + (m - j)
            if groups < ans { ans = groups }
        }
        return ans
    }
}
