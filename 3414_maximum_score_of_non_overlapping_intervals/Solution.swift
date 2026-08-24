// LeetCode 3414 - Maximum Score of Non-overlapping Intervals
// https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/

class Solution {
    func maximumWeight(_ intervals: [[Int]]) -> [Int] {
        let n = intervals.count
        var arr = [(l: Int, r: Int, w: Int, i: Int)]()
        for i in 0..<n { arr.append((intervals[i][0], intervals[i][1], intervals[i][2], i)) }
        arr.sort { $0.r < $1.r }
        struct State {
            var score: Int = 0
            var idx: [Int] = []
        }
        func better(_ a: State, _ b: State) -> State {
            if a.score != b.score { return a.score > b.score ? a : b }
            let m = min(a.idx.count, b.idx.count)
            for i in 0..<m {
                if a.idx[i] != b.idx[i] { return a.idx[i] < b.idx[i] ? a : b }
            }
            return a.idx.count <= b.idx.count ? a : b
        }
        var dp = Array(repeating: Array(repeating: State(), count: 5), count: n + 1)
        if n >= 1 {
            for i in 1...n {
                let cur = arr[i - 1]
                for t in 0...4 { dp[i][t] = dp[i - 1][t] }
                var lo = 0, hi = i - 1
                while lo < hi {
                    let mid = (lo + hi) / 2
                    if arr[mid].r < cur.l { lo = mid + 1 }
                    else { hi = mid }
                }
                let prev = lo
                for t in 1...4 {
                    var cand = dp[prev][t - 1]
                    cand.score += cur.w
                    cand.idx.append(cur.i)
                    cand.idx.sort()
                    dp[i][t] = better(dp[i][t], cand)
                }
            }
        }
        var best = dp[n][0]
        for t in 1...4 { best = better(best, dp[n][t]) }
        return best.idx
    }
}
