// LeetCode 2589 - Minimum Time to Complete All Tasks
// https://leetcode.com/problems/minimum-time-to-complete-all-tasks/

class Solution {
    func findMinimumTime(_ tasks: [[Int]]) -> Int {
        let tasks = tasks.sorted { $0[1] < $1[1] }
        var on = [Bool](repeating: false, count: 2001)
        var ans = 0
        for t in tasks {
            let start = t[0], end = t[1], dur = t[2]
            var have = 0
            for i in start...end where on[i] { have += 1 }
            var need = dur - have
            for i in stride(from: end, through: start, by: -1) where need > 0 {
                if !on[i] {
                    on[i] = true
                    need -= 1
                    ans += 1
                }
            }
        }
        return ans
    }
}
