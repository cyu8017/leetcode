// LeetCode 2184 - Number of Ways to Build Sturdy Brick Wall
// https://leetcode.com/problems/number-of-ways-to-build-sturdy-brick-wall/

class Solution {
    func buildWall(_ height: Int, _ width: Int, _ bricks: [Int]) -> Int {
        let MOD = 1_000_000_007
        var masks = [Int]()
        func gen(_ remain: Int, _ mask: Int) {
            if remain == 0 { masks.append(mask); return }
            for b in bricks where b <= remain {
                var nm = mask
                if remain - b > 0 { nm |= 1 << (remain - b) }
                gen(remain - b, nm)
            }
        }
        gen(width, 0)
        let m = masks.count
        var compat = [[Int]](repeating: [], count: m)
        for i in 0..<m {
            for j in 0..<m where (masks[i] & masks[j]) == 0 { compat[i].append(j) }
        }
        var dp = [Int](repeating: 1, count: m)
        for _ in 1..<height {
            var ndp = [Int](repeating: 0, count: m)
            for i in 0..<m {
                for j in compat[i] { ndp[j] = (ndp[j] + dp[i]) % MOD }
            }
            dp = ndp
        }
        return dp.reduce(0) { ($0 + $1) % MOD }
    }
}
