// LeetCode 2528 - Maximize the Minimum Powered City
// https://leetcode.com/problems/maximize-the-minimum-powered-city/

class Solution {
    func maxPower(_ stations: [Int], _ r: Int, _ k: Int) -> Int {
        let n = stations.count
        var diff = [Int](repeating: 0, count: n + 1)
        for i in 0..<n {
            let L = max(0, i - r)
            let R = min(n - 1, i + r)
            diff[L] += stations[i]
            diff[R + 1] -= stations[i]
        }
        var power = [Int](repeating: 0, count: n)
        var cur = 0
        for i in 0..<n {
            cur += diff[i]
            power[i] = cur
        }
        func ok(_ x: Int) -> Bool {
            var extra = [Int](repeating: 0, count: n + 1)
            var have = 0, used = 0
            for i in 0..<n {
                have += extra[i]
                let need = x - (power[i] + have)
                if need > 0 {
                    used += need
                    if used > k { return false }
                    have += need
                    let end = i + 2 * r
                    if end + 1 <= n { extra[end + 1] -= need }
                }
            }
            return true
        }
        var lo = 0, hi = k
        for p in power { hi = max(hi, p) }
        hi += k
        while lo < hi {
            let mid = (lo + hi + 1) / 2
            if ok(mid) { lo = mid } else { hi = mid - 1 }
        }
        return lo
    }
}
