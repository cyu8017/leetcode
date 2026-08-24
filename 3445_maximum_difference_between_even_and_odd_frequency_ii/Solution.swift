// LeetCode 3445 - Maximum Difference Between Even and Odd Frequency II
// https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/

class Solution {
    func maxDifference(_ s: String, _ k: Int) -> Int {
        let chars = Array(s)
        let n = chars.count
        var ans = -1_000_000_000
        for a in 0..<5 {
            for b in 0..<5 where a != b {
                var prefA = Array(repeating: 0, count: n + 1)
                var prefB = Array(repeating: 0, count: n + 1)
                for i in 0..<n {
                    prefA[i + 1] = prefA[i]
                    prefB[i + 1] = prefB[i]
                    if Int(chars[i].asciiValue! - 48) == a { prefA[i + 1] += 1 }
                    if Int(chars[i].asciiValue! - 48) == b { prefB[i + 1] += 1 }
                }
                for i in 0..<n {
                    var j = i + k - 1
                    while j < n {
                        let fa = prefA[j + 1] - prefA[i]
                        let fb = prefB[j + 1] - prefB[i]
                        if fa % 2 == 1 && fb % 2 == 0 && fb > 0 {
                            if fa - fb > ans { ans = fa - fb }
                        }
                        j += 1
                    }
                }
            }
        }
        return ans
    }
}
