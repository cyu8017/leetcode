// LeetCode 3312 - Sorted GCD Pair Queries
// https://leetcode.com/problems/sorted-gcd-pair-queries/

class Solution {
    func gcdValues(_ nums: [Int], _ queries: [Int]) -> [Int] {
        var maxV = 0
        for x in nums where x > maxV { maxV = x }
        var cnt = Array(repeating: 0, count: maxV + 1)
        for x in nums { cnt[x] += 1 }
        var divCnt = Array(repeating: 0, count: maxV + 1)
        for g in 1...maxV {
            var c = 0
            var m = g
            while m <= maxV {
                c += cnt[m]
                m += g
            }
            divCnt[g] = c * (c - 1) / 2
        }
        var exact = Array(repeating: 0, count: maxV + 1)
        for g in stride(from: maxV, through: 1, by: -1) {
            exact[g] = divCnt[g]
            var m = 2 * g
            while m <= maxV {
                exact[g] -= exact[m]
                m += g
            }
        }
        var pref = Array(repeating: 0, count: maxV + 1)
        for g in 1...maxV { pref[g] = pref[g - 1] + exact[g] }
        var ans = Array(repeating: 0, count: queries.count)
        for i in 0..<queries.count {
            let q = queries[i]
            var lo = 1, hi = maxV
            while lo < hi {
                let mid = (lo + hi) / 2
                if pref[mid] > q { hi = mid }
                else { lo = mid + 1 }
            }
            ans[i] = lo
        }
        return ans
    }
}
