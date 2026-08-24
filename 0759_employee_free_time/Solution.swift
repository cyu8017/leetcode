// LeetCode 0759 - Employee Free Time
// https://leetcode.com/problems/employee-free-time/

class Solution {
    func employeeFreeTime(_ schedule: [[[Int]]]) -> [[Int]] {
        var intervals = [[Int]]()
        for employee in schedule { intervals.append(contentsOf: employee) }
        intervals.sort { $0[0] < $1[0] }
        var merged = [[Int]]()
        for iv in intervals {
            if merged.isEmpty || merged[merged.count - 1][1] < iv[0] {
                merged.append(iv)
            } else {
                merged[merged.count - 1][1] = max(merged[merged.count - 1][1], iv[1])
            }
        }
        var result = [[Int]]()
        if merged.count >= 2 {
            for i in 1..<merged.count {
                result.append([merged[i - 1][1], merged[i][0]])
            }
        }
        return result
    }
}
