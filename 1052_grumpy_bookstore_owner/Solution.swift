// LeetCode 1052 - Grumpy Bookstore Owner
// https://leetcode.com/problems/grumpy-bookstore-owner/

class Solution {
    func maxSatisfied(_ customers: [Int], _ grumpy: [Int], _ minutes: Int) -> Int {
        var base = 0
        for i in 0..<customers.count {
            if grumpy[i] == 0 {
                base += customers[i]
            }
        }
        var gain = 0
        var best = 0
        for i in 0..<customers.count {
            if grumpy[i] == 1 {
                gain += customers[i]
            }
            if i >= minutes && grumpy[i - minutes] == 1 {
                gain -= customers[i - minutes]
            }
            best = max(best, gain)
        }
        return base + best
    }
}
