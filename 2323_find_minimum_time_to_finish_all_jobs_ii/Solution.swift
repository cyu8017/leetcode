// LeetCode 2323 - Find Minimum Time to Finish All Jobs II
// https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs-ii/

class Solution {
    func minimumTime(_ jobs: [Int], _ workers: [Int]) -> Int {
        let jobs = jobs.sorted()
        let workers = workers.sorted()
        var ans = 0
        for i in 0..<jobs.count {
            ans = max(ans, (jobs[i] + workers[i] - 1) / workers[i])
        }
        return ans
    }
}
