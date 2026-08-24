// LeetCode 3542 - Minimum Operations to Convert All Elements to Zero
// https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let mut stk = Vec::new();
        let mut ans = 0;
        for x in nums {
            while !stk.is_empty() && *stk.last().unwrap() > x {
                ans += 1;
                stk.pop();
            }
            if x != 0 && (stk.is_empty() || *stk.last().unwrap() != x) {
                stk.push(x);
            }
        }
        ans + stk.len() as i32
    }
}
