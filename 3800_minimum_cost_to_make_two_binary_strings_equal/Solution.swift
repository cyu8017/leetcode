// LeetCode 3800 - Minimum Cost To Make Two Binary Strings Equal
// https://leetcode.com/problems/minimum-cost-to-make-two-binary-strings-equal/

class Solution {
    func minimumCost(_ s: String, _ t: String, _ flipCost: Int, _ swapCost: Int, _ crossCost: Int) -> Int {
        let sc = Array(s), tc = Array(t)
        var diff = [0, 0]
        for i in 0..<sc.count {
            if sc[i] != tc[i] { diff[Int(sc[i].asciiValue! - 48)] += 1 }
        }
        var ans = (diff[0] + diff[1]) * flipCost
        let mx = max(diff[0], diff[1])
        let mn = min(diff[0], diff[1])
        ans = min(ans, mn * swapCost + (mx - mn) * flipCost)
        let avg = (mx + mn) / 2
        ans = min(ans, (avg - mn) * crossCost + avg * swapCost + (mx + mn - avg * 2) * flipCost)
        return ans
    }
}
