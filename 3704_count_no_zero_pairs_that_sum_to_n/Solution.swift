// LeetCode 3704 - Count No-Zero Pairs That Sum to N
// https://leetcode.com/problems/count-no-zero-pairs-that-sum-to-n/

class Solution {
    func countNoZeroPairs(_ n: Int) -> Int {
        let s = Array(String(n))
        let m = s.count
        var digits = Array(repeating: 0, count: m + 1)
        for i in 0..<m { digits[i] = Int(s[m - 1 - i].asciiValue! - 48) }
        var dp = Array(repeating: Array(repeating: [0, 0], count: 2), count: 2)
        dp[0][1][1] = 1
        for pos in 0..<(m + 1) {
            var ndp = Array(repeating: Array(repeating: [0, 0], count: 2), count: 2)
            let target = digits[pos]
            for carry in 0...1 {
                for aliveA in 0...1 {
                    for aliveB in 0...1 {
                        let ways = dp[carry][aliveA][aliveB]
                        if ways == 0 { continue }
                        var A = [[Int]]()
                        if aliveA == 1 {
                            for d in 1...9 { A.append([d, 1]) }
                            if pos > 0 { A.append([0, 0]) }
                        } else {
                            A.append([0, 0])
                        }
                        var B = [[Int]]()
                        if aliveB == 1 {
                            for d in 1...9 { B.append([d, 1]) }
                            if pos > 0 { B.append([0, 0]) }
                        } else {
                            B.append([0, 0])
                        }
                        for ai in A {
                            let da = ai[0], na = ai[1]
                            for bi in B {
                                let db = bi[0], nb = bi[1]
                                let sum = da + db + carry
                                if sum % 10 != target { continue }
                                let ncarry = sum / 10
                                ndp[ncarry][na][nb] += ways
                            }
                        }
                    }
                }
            }
            dp = ndp
        }
        return dp[0][0][0]
    }
}
