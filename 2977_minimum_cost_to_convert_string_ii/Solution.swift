// LeetCode 2977 - Minimum Cost to Convert String II
// https://leetcode.com/problems/minimum-cost-to-convert-string-ii/

class Solution {
    func minimumCost(_ source: String, _ target: String, _ original: [String], _ changed: [String], _ cost: [Int]) -> Int {
        let inf = 1 << 60
        var ids: [String: Int] = [:]
        for i in 0..<original.count {
            if ids[original[i]] == nil { ids[original[i]] = ids.count }
            if ids[changed[i]] == nil { ids[changed[i]] = ids.count }
        }
        let m = ids.count
        var dist = Array(repeating: Array(repeating: inf, count: m), count: m)
        for i in 0..<m { dist[i][i] = 0 }
        for i in 0..<original.count {
            let u = ids[original[i]]!, v = ids[changed[i]]!
            dist[u][v] = min(dist[u][v], cost[i])
        }
        for k in 0..<m {
            for i in 0..<m {
                for j in 0..<m {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                }
            }
        }
        let n = source.count
        var dp = Array(repeating: inf, count: n + 1)
        dp[0] = 0
        let lens = Set(ids.keys.map { $0.count })
        let sArr = Array(source), tArr = Array(target)
        for i in 0..<n {
            if dp[i] >= inf / 2 { continue }
            if sArr[i] == tArr[i] { dp[i + 1] = min(dp[i + 1], dp[i]) }
            for L in lens {
                if i + L > n { continue }
                let ss = String(sArr[i..<(i + L)])
                let tt = String(tArr[i..<(i + L)])
                guard let iu = ids[ss], let iv = ids[tt] else { continue }
                if dist[iu][iv] < inf / 2 {
                    dp[i + L] = min(dp[i + L], dp[i] + dist[iu][iv])
                }
            }
        }
        return dp[n] >= inf / 2 ? -1 : dp[n]
    }
}
