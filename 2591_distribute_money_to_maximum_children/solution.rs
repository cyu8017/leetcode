// LeetCode 2591 - Distribute Money to Maximum Children
// https://leetcode.com/problems/distribute-money-to-maximum-children/

impl Solution {
    pub fn dist_money(mut money: i32, children: i32) -> i32 {
        if money < children {
            return -1;
        }
        money -= children;
        let mut ans = money / 7;
        if ans > children {
            ans = children;
        }
        let remain_money = money - ans * 7;
        let remain_child = children - ans;
        if remain_child == 0 && remain_money > 0 {
            ans -= 1;
        } else if remain_child == 1 && remain_money == 3 {
            ans -= 1;
        }
        if ans < 0 {
            0
        } else {
            ans
        }
    }
}
