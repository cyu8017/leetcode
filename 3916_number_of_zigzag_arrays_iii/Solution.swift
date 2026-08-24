// LeetCode 3916 - Number of ZigZag Arrays III
// https://leetcode.com/problems/number-of-zigzag-arrays-iii/

class Solution {
    func zigZagArrays(_ n: Int, _ l: Int, _ r: Int) -> Int {
        let mod = 1_000_000_007
        let points = n + 1
        var values = [Int](repeating: 0, count: points + 1)
        for m in 1...points {
            var up = [Int](repeating: 0, count: m)
            var down = [Int](repeating: 0, count: m)
            for value in 0..<m {
                up[value] = value
                down[value] = m - 1 - value
            }
            if n >= 3 {
                for _ in 3...n {
                    var nextUp = [Int](repeating: 0, count: m)
                    var nextDown = [Int](repeating: 0, count: m)
                    var prefix = 0
                    for value in 0..<m {
                        nextUp[value] = prefix
                        prefix = (prefix + down[value]) % mod
                    }
                    var suffix = 0
                    for value in stride(from: m - 1, through: 0, by: -1) {
                        nextDown[value] = suffix
                        suffix = (suffix + up[value]) % mod
                    }
                    up = nextUp
                    down = nextDown
                }
            }
            for value in 0..<m {
                values[m] = (values[m] + up[value] + down[value]) % mod
            }
        }
        let x = (r - l + 1) % mod
        if r - l + 1 <= points { return values[r - l + 1] }
        var prefixA = [Int](repeating: 0, count: points + 2)
        var suffixA = [Int](repeating: 0, count: points + 2)
        prefixA[0] = 1
        for i in 1...points {
            prefixA[i] = prefixA[i - 1] * ((x - i + mod) % mod) % mod
        }
        suffixA[points + 1] = 1
        for i in stride(from: points, through: 1, by: -1) {
            suffixA[i] = suffixA[i + 1] * ((x - i + mod) % mod) % mod
        }
        var factorial = [Int](repeating: 0, count: points + 1)
        factorial[0] = 1
        for i in 1...points { factorial[i] = factorial[i - 1] * i % mod }
        var answer = 0
        for i in 1...points {
            let numerator = prefixA[i - 1] * suffixA[i + 1] % mod
            let denominator = factorial[i - 1] * factorial[points - i] % mod
            let term = values[i] * numerator % mod * powm(denominator, mod - 2, mod) % mod
            if (points - i) % 2 == 1 { answer -= term }
            else { answer += term }
            answer %= mod
        }
        if answer < 0 { answer += mod }
        return answer
    }

    private func powm(_ a: Int, _ e: Int, _ mod: Int) -> Int {
        var a = a, e = e, res = 1
        while e > 0 {
            if (e & 1) != 0 { res = res * a % mod }
            a = a * a % mod
            e >>= 1
        }
        return res
    }
}
