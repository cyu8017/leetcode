// LeetCode 3540 - Minimum Time to Visit All Houses
// https://leetcode.com/problems/minimum-time-to-visit-all-houses/

class Solution {
    func minTotalTime(_ forward: [Int], _ backward: [Int], _ queries: [Int]) -> Int {
        let n = forward.count
        var sumB = 0
        for v in backward { sumB += v }
        var pf = Array(repeating: 0, count: n + 1)
        var pb = Array(repeating: 0, count: n + 1)
        for i in 0..<n {
            pf[i + 1] = pf[i] + forward[i]
            pb[i + 1] = pb[i] + backward[i]
        }
        var ans = 0
        var pos = 0
        for q in queries {
            var r = 0
            if q < pos { r = pf[n] }
            r += pf[q] - pf[pos]
            var l = 0
            if q > pos { l = sumB }
            l += pb[pos] - pb[q]
            ans += min(l, r)
            pos = q
        }
        return ans
    }
}
