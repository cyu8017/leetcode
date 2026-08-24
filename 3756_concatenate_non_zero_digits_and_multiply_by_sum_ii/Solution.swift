// LeetCode 3756 - Concatenate Non Zero Digits And Multiply By Sum II
// https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/

class Solution {
    private static let MX = 100001
    private static let MOD = 1_000_000_007
    private static let PW: [Int] = {
        var pw = [Int](repeating: 0, count: 100001)
        pw[0] = 1
        for i in 1..<100001 { pw[i] = pw[i - 1] * 10 % 1_000_000_007 }
        return pw
    }()

    func sumAndMultiply(_ s: String, _ queries: [[Int]]) -> [Int] {
        let chars = Array(s)
        let n = chars.count
        var sumD = [Int](repeating: 0, count: n + 1)
        var cntN0 = [Int](repeating: 0, count: n + 1)
        var p = [Int](repeating: 0, count: n + 1)
        let MOD = 1_000_000_007
        for i in 1...n {
            let d = Int(chars[i - 1].asciiValue! - 48)
            sumD[i] = sumD[i - 1] + d
            cntN0[i] = cntN0[i - 1]
            if d > 0 {
                cntN0[i] += 1
                p[i] = (p[i - 1] * 10 + d) % MOD
            } else {
                p[i] = p[i - 1]
            }
        }
        var ans = [Int](repeating: 0, count: queries.count)
        for i in 0..<queries.count {
            let l = queries[i][0], r = queries[i][1]
            let n0 = cntN0[r + 1] - cntN0[l]
            let sd = sumD[r + 1] - sumD[l]
            let x = (p[r + 1] - p[l] * Solution.PW[n0] % MOD + MOD) % MOD
            ans[i] = x * sd % MOD
        }
        return ans
    }
}
