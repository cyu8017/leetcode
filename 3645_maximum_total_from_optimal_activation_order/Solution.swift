// LeetCode 3645 - Maximum Total from Optimal Activation Order
// https://leetcode.com/problems/maximum-total-from-optimal-activation-order/

class Solution {
    func maxTotal(_ value: [Int], _ limit: [Int]) -> Int {
        var g = [Int: [Int]]()
        for i in 0..<value.count { g[limit[i], default: []].append(value[i]) }
        var ans = 0
        for (lim, vs0) in g {
            var vs = vs0.sorted(by: >)
            for i in 0..<min(lim, vs.count) { ans += vs[i] }
        }
        return ans
    }
}
