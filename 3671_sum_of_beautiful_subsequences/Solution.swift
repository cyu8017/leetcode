// LeetCode 3671 - Sum of Beautiful Subsequences
// https://leetcode.com/problems/sum-of-beautiful-subsequences/

class Solution {
    func totalBeauty(_ nums: [Int]) -> Int {
        let MOD = 1_000_000_007
        var mx = 0
        for v in nums { mx = max(mx, v) }
        var pos = Array(repeating: [Int](), count: mx + 1)
        for i in 0..<nums.count { pos[nums[i]].append(i) }
        var cnt = Array(repeating: 0, count: mx + 1)
        if mx >= 1 {
            for g in 1...mx {
                var seq = [Int]()
                var m = g
                while m <= mx { seq.append(contentsOf: pos[m]); m += g }
                if seq.isEmpty { continue }
                seq.sort()
                var ways = 1
                for _ in 0..<seq.count { ways = ways * 2 % MOD }
                cnt[g] = (ways - 1 + MOD) % MOD
            }
        }
        var ans = 0
        if mx >= 1 {
            for g in stride(from: mx, through: 1, by: -1) {
                var m = 2 * g
                while m <= mx {
                    cnt[g] = (cnt[g] - cnt[m] + MOD) % MOD
                    m += g
                }
                ans = (ans + cnt[g] * g) % MOD
            }
        }
        return ans
    }
}
