// LeetCode 3668 - Restore Finishing Order
// https://leetcode.com/problems/restore-finishing-order/

impl Solution {
    pub fn recover_order(order: Vec<i32>, mut friends: Vec<i32>) -> Vec<i32> {
        let n = order.len();
        let mut d = vec![0; n + 1];
        for (i, &x) in order.iter().enumerate() {
            d[x as usize] = i;
        }
        friends.sort_by_key(|&a| d[a as usize]);
        friends
    }
}
