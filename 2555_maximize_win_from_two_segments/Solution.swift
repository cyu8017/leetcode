// LeetCode 2555 - Maximize Win From Two Segments
// https://leetcode.com/problems/maximize-win-from-two-segments/

class Solution {
    func maximizeWin(_ prizePositions: [Int], _ k: Int) -> Int {
        let n = prizePositions.count
        var dp = [Int](repeating: 0, count: n + 1)
        var ans = 0, left = 0
        for right in 0..<n {
            while prizePositions[right] - prizePositions[left] > k { left += 1 }
            let cur = right - left + 1
            ans = max(ans, dp[left] + cur)
            dp[right + 1] = max(dp[right], cur)
        }
        return ans
    }
}
