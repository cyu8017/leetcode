// LeetCode 3636 - Threshold Majority Queries
// https://leetcode.com/problems/threshold-majority-queries/

class Solution {
    func subarrayMajority(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        var ans = Array(repeating: 0, count: queries.count)
        for qi in 0..<queries.count {
            let l = queries[qi][0], r = queries[qi][1], t = queries[qi][2]
            var cnt = [Int: Int]()
            for i in l...r { cnt[nums[i], default: 0] += 1 }
            var best = -1, bestC = 0
            for (v, c) in cnt {
                if c >= t && (c > bestC || (c == bestC && (best == -1 || v < best))) {
                    bestC = c
                    best = v
                }
            }
            ans[qi] = best
        }
        return ans
    }
}
