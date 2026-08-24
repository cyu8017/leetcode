// LeetCode 2073 - Time Needed to Buy Tickets
// https://leetcode.com/problems/time-needed-to-buy-tickets/

impl Solution {
    pub fn time_required_to_buy(tickets: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let mut ans = 0;
        for i in 0..tickets.len() {
            if i <= k {
                ans += tickets[i].min(tickets[k]);
            } else {
                ans += tickets[i].min(tickets[k] - 1);
            }
        }
        ans
    }
}
