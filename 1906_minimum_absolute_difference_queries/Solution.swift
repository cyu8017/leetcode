// LeetCode 1906 - Minimum Absolute Difference Queries
// https://leetcode.com/problems/minimum-absolute-difference-queries/

class Solution {
    func minDifference(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        let n = nums.count
        var pref = Array(repeating: Array(repeating: 0, count: 101), count: n + 1)
        for i in 0..<n {
            pref[i + 1] = pref[i]
            pref[i + 1][nums[i]] += 1
        }
        var ans: [Int] = []
        for q in queries {
            let left = q[0], right = q[1]
            var prev = -1
            var best = Int.max
            for value in 1...100 {
                if pref[right + 1][value] - pref[left][value] > 0 {
                    if prev != -1 { best = min(best, value - prev) }
                    prev = value
                }
            }
            ans.append(best == Int.max ? -1 : best)
        }
        return ans
    }
}
