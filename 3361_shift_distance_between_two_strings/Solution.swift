// LeetCode 3361 - Shift Distance Between Two Strings
// https://leetcode.com/problems/shift-distance-between-two-strings/

class Solution {
    func shiftDistance(_ s: String, _ t: String, _ nextCost: [Int], _ previousCost: [Int]) -> Int {
        let sa = Array(s), ta = Array(t)
        var ans = 0
        for i in 0..<sa.count {
            var a = Int(sa[i].asciiValue! - 97)
            let b = Int(ta[i].asciiValue! - 97)
            if a == b { continue }
            var fwd = 0
            var x = a
            while x != b {
                fwd += nextCost[x]
                x = (x + 1) % 26
            }
            var bwd = 0
            x = a
            while x != b {
                bwd += previousCost[x]
                x = (x + 25) % 26
            }
            ans += min(fwd, bwd)
        }
        return ans
    }
}
