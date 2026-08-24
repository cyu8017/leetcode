// LeetCode 2223 - Sum of Scores of Built Strings
// https://leetcode.com/problems/sum-of-scores-of-built-strings/

class Solution {
    func sumScores(_ s: String) -> Int {
        let arr = Array(s)
        let n = arr.count
        var z = [Int](repeating: 0, count: n)
        var l = 0, r = 0
        if n > 1 {
            for i in 1..<n {
                if i <= r { z[i] = min(r - i + 1, z[i - l]) }
                while i + z[i] < n && arr[z[i]] == arr[i + z[i]] { z[i] += 1 }
                if i + z[i] - 1 > r {
                    l = i
                    r = i + z[i] - 1
                }
            }
        }
        return n + z.reduce(0, +)
    }
}
