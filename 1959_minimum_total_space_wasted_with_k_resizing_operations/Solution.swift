// LeetCode 1959 - Minimum Total Space Wasted With K Resizing Operations
// https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/

class Solution {
    func minSpaceWastedKResizing(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        let INF = Int.max / 4
        var waste = Array(repeating: Array(repeating: 0, count: n), count: n)
        for i in 0..<n {
            var mx = 0, total = 0
            for j in i..<n {
                mx = max(mx, nums[j])
                total += nums[j]
                waste[i][j] = mx * (j - i + 1) - total
            }
        }
        let segments = k + 1
        var dp = Array(repeating: Array(repeating: INF, count: segments + 1), count: n + 1)
        dp[0][0] = 0
        for i in 1...n {
            for s in 1...min(segments, i) {
                for p in (s - 1)..<i {
                    dp[i][s] = min(dp[i][s], dp[p][s - 1] + waste[p][i - 1])
                }
            }
        }
        return (1...segments).map { dp[n][$0] }.min()!
    }
}
