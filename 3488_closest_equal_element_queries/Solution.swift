// LeetCode 3488 - Closest Equal Element Queries
// https://leetcode.com/problems/closest-equal-element-queries/

class Solution {
    func solveQueries(_ nums: [Int], _ queries: [Int]) -> [Int] {
        let n = nums.count
        var pos = [Int: [Int]]()
        for i in 0..<n { pos[nums[i], default: []].append(i) }
        var ans = Array(repeating: 0, count: queries.count)
        for qi in 0..<queries.count {
            let idx = queries[qi]
            let arr = pos[nums[idx]]!
            if arr.count == 1 { ans[qi] = -1; continue }
            var best = n
            for p in arr where p != idx {
                var d = abs(p - idx)
                d = min(d, n - d)
                if d < best { best = d }
            }
            ans[qi] = best
        }
        return ans
    }
}
