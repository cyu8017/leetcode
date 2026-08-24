// LeetCode 3538 - Merge Operations for Minimum Travel Time
// https://leetcode.com/problems/merge-operations-for-minimum-travel-time/

class Solution {
    var n = 0, k = 0
    var position = [Int]()
    var prefix = [Int]()
    var memo = [String: Int]()
    let INF = Int.max / 4

    func minTravelTime(_ l: Int, _ n: Int, _ k: Int, _ position: [Int], _ time: [Int]) -> Int {
        self.n = n
        self.k = k
        self.position = position
        prefix = Array(repeating: 0, count: n)
        prefix[0] = time[0]
        if n > 1 {
            for i in 1..<n { prefix[i] = prefix[i - 1] + time[i] }
        }
        memo = [:]
        return dp(0, k, 0)
    }

    func dp(_ i: Int, _ skips: Int, _ last: Int) -> Int {
        if i == n - 1 { return skips == 0 ? 0 : INF }
        let key = "\(i),\(skips),\(last)"
        if let v = memo[key] { return v }
        var rate = prefix[i]
        if last > 0 { rate -= prefix[last - 1] }
        var res = INF
        var end = n - 1
        if i + skips + 1 < end { end = i + skips + 1 }
        if i + 1 <= end {
            for j in (i + 1)...end {
                let cand = (position[j] - position[i]) * rate + dp(j, skips - (j - i - 1), i + 1)
                if cand < res { res = cand }
            }
        }
        memo[key] = res
        return res
    }
}
