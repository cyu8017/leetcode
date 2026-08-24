// LeetCode 0826 - Most Profit Assigning Work
// https://leetcode.com/problems/most-profit-assigning-work/

class Solution {
    func maxProfitAssignment(_ difficulty: [Int], _ profit: [Int], _ worker: [Int]) -> Int {
        let jobs = zip(difficulty, profit).map { ($0, $1) }.sorted { $0.0 < $1.0 }
        let workers = worker.sorted()
        var ans = 0, best = 0, i = 0
        for ability in workers {
            while i < jobs.count && jobs[i].0 <= ability {
                best = max(best, jobs[i].1)
                i += 1
            }
            ans += best
        }
        return ans
    }
}
