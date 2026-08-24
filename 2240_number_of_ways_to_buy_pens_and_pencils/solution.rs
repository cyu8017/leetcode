// LeetCode 2240 - Number of Ways to Buy Pens and Pencils
// https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/

impl Solution {
    pub fn ways_to_buy_pens_pencils(total: i32, cost1: i32, cost2: i32) -> i64 {
        let mut ans = 0i64;
        let mut pens = 0;
        while pens * cost1 <= total {
            let remain = total - pens * cost1;
            ans += (remain / cost2 + 1) as i64;
            pens += 1;
        }
        ans
    }
}
