// LeetCode 2073 - Time Needed to Buy Tickets
// https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution {
    func timeRequiredToBuy(_ tickets: [Int], _ k: Int) -> Int {
        var ans = 0
        for i in 0..<tickets.count {
            if i <= k { ans += min(tickets[i], tickets[k]) }
            else { ans += min(tickets[i], tickets[k] - 1) }
        }
        return ans
    }
}
