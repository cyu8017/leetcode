// LeetCode 1229 - Meeting Scheduler
// https://leetcode.com/problems/meeting-scheduler/

class Solution {
    func minAvailableDuration(_ slots1: [[Int]], _ slots2: [[Int]], _ duration: Int) -> [Int] {
        let a = slots1.sorted { $0[0] < $1[0] }
        let b = slots2.sorted { $0[0] < $1[0] }
        var i = 0, j = 0
        while i < a.count && j < b.count {
            let start = max(a[i][0], b[j][0])
            let end = min(a[i][1], b[j][1])
            if end - start >= duration { return [start, start + duration] }
            if a[i][1] < b[j][1] { i += 1 } else { j += 1 }
        }
        return []
    }
}
