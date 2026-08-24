// LeetCode 3668 - Restore Finishing Order
// https://leetcode.com/problems/restore-finishing-order/

class Solution {
    func recoverOrder(_ order: [Int], _ friends: [Int]) -> [Int] {
        var d = Array(repeating: 0, count: order.count + 1)
        for i in 0..<order.count { d[order[i]] = i }
        return friends.sorted { d[$0] < d[$1] }
    }
}
