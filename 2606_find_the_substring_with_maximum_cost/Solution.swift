// LeetCode 2606 - Find the Substring With Maximum Cost
// https://leetcode.com/problems/find-the-substring-with-maximum-cost/

class Solution {
    func maximumCostSubstring(_ s: String, _ chars: String, _ vals: [Int]) -> Int {
        var val = Array(1...26)
        let cc = Array(chars)
        for i in 0..<cc.count {
            val[Int(cc[i].asciiValue! - Character("a").asciiValue!)] = vals[i]
        }
        var best = 0, cur = 0
        for c in s {
            cur += val[Int(c.asciiValue! - Character("a").asciiValue!)]
            if cur < 0 { cur = 0 }
            best = max(best, cur)
        }
        return best
    }
}
