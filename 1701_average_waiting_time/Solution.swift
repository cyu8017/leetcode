// LeetCode 1701 - Average Waiting Time
// https://leetcode.com/problems/average-waiting-time/

class Solution {
    func averageWaitingTime(_ customers: [[Int]]) -> Double {
        var current = 0
        var total = 0
        for customer in customers {
            current = max(current, customer[0]) + customer[1]
            total += current - customer[0]
        }
        return Double(total) / Double(customers.count)
    }
}
