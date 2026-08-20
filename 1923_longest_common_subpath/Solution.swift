// LeetCode 1923 - Longest Common Subpath
// https://leetcode.com/problems/longest-common-subpath/

class Solution {
    func longestCommonSubpath(_ n: Int, _ paths: [[Int]]) -> Int {
        let BASE1 = 911_382_323, MOD1 = 1_000_000_007
        let BASE2 = 972_663_749, MOD2 = 1_000_000_009
        func modPow(_ base: Int, _ exp: Int, _ mod: Int) -> Int {
            var b = base % mod, e = exp, r = 1
            while e > 0 {
                if e & 1 == 1 { r = r * b % mod }
                b = b * b % mod
                e >>= 1
            }
            return r
        }
        func hasCommon(_ length: Int) -> Bool {
            if length == 0 { return true }
            var common: Set<Int64>? = nil
            let pow1 = modPow(BASE1, length, MOD1)
            let pow2 = modPow(BASE2, length, MOD2)
            for path in paths {
                if path.count < length { return false }
                var h1 = 0, h2 = 0
                var seen = Set<Int64>()
                for i in 0..<path.count {
                    h1 = (h1 * BASE1 + path[i] + 1) % MOD1
                    h2 = (h2 * BASE2 + path[i] + 1) % MOD2
                    if i >= length {
                        h1 = (h1 - (path[i - length] + 1) * pow1 % MOD1 + MOD1) % MOD1
                        h2 = (h2 - (path[i - length] + 1) * pow2 % MOD2 + MOD2) % MOD2
                    }
                    if i >= length - 1 {
                        seen.insert(Int64(h1) << 32 | Int64(h2))
                    }
                }
                if common == nil {
                    common = seen
                } else {
                    common = common!.intersection(seen)
                }
                if common!.isEmpty { return false }
            }
            return true
        }
        var lo = 0, hi = paths.map { $0.count }.min()!
        while lo < hi {
            let mid = (lo + hi + 1) / 2
            if hasCommon(mid) { lo = mid } else { hi = mid - 1 }
        }
        return lo
    }
}
