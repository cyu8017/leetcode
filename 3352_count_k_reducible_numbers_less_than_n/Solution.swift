// LeetCode 3352 - Count K-Reducible Numbers Less Than N
// https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/

class Solution {
    func countKReducibleNumbers(_ s: String, _ k: Int) -> Int {
        let mod = 1_000_000_007
        let chars = Array(s)
        var red = Array(repeating: 0, count: 801)
        func bitsPop(_ x: Int) -> Int {
            var x = x, c = 0
            while x > 0 { c += x & 1; x >>= 1 }
            return c
        }
        if 2 <= 800 {
            for i in 2...800 { red[i] = 1 + red[bitsPop(i)] }
        }
        var memo = [Int: Int]()
        func key(_ pos: Int, _ tight: Int, _ ones: Int) -> Int {
            return (pos << 32) | (tight << 16) | ones
        }
        func dfs(_ pos: Int, _ tight: Bool, _ ones: Int) -> Int {
            if pos == chars.count {
                if ones == 0 { return 0 }
                return red[ones] <= k - 1 ? 1 : 0
            }
            let ky = key(pos, tight ? 1 : 0, ones)
            if let v = memo[ky] { return v }
            let up = tight ? Int(chars[pos].asciiValue! - 48) : 1
            var ans = 0
            for d in 0...up {
                let nt = tight && d == up
                ans = (ans + dfs(pos + 1, nt, ones + d)) % mod
            }
            memo[ky] = ans
            return ans
        }
        return dfs(0, true, 0)
    }
}
