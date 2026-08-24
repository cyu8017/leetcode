// LeetCode 3743 - Maximize Cyclic Partition Score
// https://leetcode.com/problems/maximize-cyclic-partition-score/

class Solution {
    func maximumScore(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var a = nums + nums
        var kk = k
        if kk > n { kk = n }
        var best = 0
        let NEG = -(1 << 60)
        for start in 0..<n {
            let seg = Array(a[start..<(start + n)])
            var dp = Array(repeating: [Int](repeating: NEG, count: kk + 1), count: n + 1)
            dp[0][0] = 0
            for i in 1...n {
                let jmax = min(kk, i)
                if jmax >= 1 {
                    for j in 1...jmax {
                        var mx = NEG
                        for t in stride(from: i, through: j, by: -1) {
                            if seg[t - 1] > mx { mx = seg[t - 1] }
                            if dp[t - 1][j - 1] > NEG {
                                let cand = dp[t - 1][j - 1] + mx
                                if cand > dp[i][j] { dp[i][j] = cand }
                            }
                        }
                    }
                }
            }
            if dp[n][kk] > best { best = dp[n][kk] }
        }
        return best
    }
}
