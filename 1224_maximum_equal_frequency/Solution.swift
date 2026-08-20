// LeetCode 1224 - Maximum Equal Frequency
// https://leetcode.com/problems/maximum-equal-frequency/

class Solution {
    func maxEqualFreq(_ nums: [Int]) -> Int {
        var count: [Int: Int] = [:]
        var freq: [Int: Int] = [:]
        var ans = 0
        for (i, x) in nums.enumerated() {
            if let c = count[x], c > 0 {
                freq[c]! -= 1
                if freq[c] == 0 { freq[c] = nil }
            }
            count[x, default: 0] += 1
            let c = count[x]!
            freq[c, default: 0] += 1
            if freq.count == 1 {
                let (f, n) = freq.first!
                if f == 1 || n == 1 { ans = i + 1 }
            } else if freq.count == 2 {
                let keys = Array(freq.keys).sorted()
                let f1 = keys[0], f2 = keys[1]
                if (f1 == 1 && freq[f1] == 1) || (f2 == f1 + 1 && freq[f2] == 1) {
                    ans = i + 1
                }
            }
        }
        return ans
    }
}
