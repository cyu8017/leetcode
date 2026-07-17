// LeetCode 1723 - Find Minimum Time to Finish All Jobs
// https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/

class Solution {
    func minimumTimeRequired(_ jobs: [Int], _ k: Int) -> Int {
        let sorted = jobs.sorted(by: >)
        var loads = [Int](repeating: 0, count: k)
        var best = sorted.reduce(0, +)

        func backtrack(_ i: Int) {
            if i == sorted.count {
                best = min(best, loads.max()!)
                return
            }
            var seen = Set<Int>()
            for worker in 0..<k {
                if seen.contains(loads[worker]) {
                    continue
                }
                if loads[worker] + sorted[i] >= best {
                    continue
                }
                seen.insert(loads[worker])
                loads[worker] += sorted[i]
                backtrack(i + 1)
                loads[worker] -= sorted[i]
                if loads[worker] == 0 {
                    break
                }
            }
        }

        backtrack(0)
        return best
    }
}
