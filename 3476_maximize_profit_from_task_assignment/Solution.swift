// LeetCode 3476 - Maximize Profit from Task Assignment
// https://leetcode.com/problems/maximize-profit-from-task-assignment/

class Solution {
    func maxProfit(_ workers: [Int], _ tasks: [[Int]]) -> Int {
        let workers = workers.sorted()
        let tasks = tasks.sorted { $0[0] < $1[0] }
        var ans = 0
        var used = Array(repeating: false, count: tasks.count)
        for w in workers {
            var best = -1, bi = -1
            for i in 0..<tasks.count {
                if used[i] { continue }
                if tasks[i][0] > w { break }
                if tasks[i][1] > best {
                    best = tasks[i][1]
                    bi = i
                }
            }
            if bi >= 0 {
                used[bi] = true
                ans += best
            }
        }
        return ans
    }
}
